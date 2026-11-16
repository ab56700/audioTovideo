
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import AudioUploadForm
from .models import UploadedAudio
from .pipeline.generate_scenes import generate_scenes
from .pipeline.generate_images import generate_images
from .pipeline.make_video import create_video
from django.conf import settings
import os


def home(request):
    return render(request, "home.html")


def dashboard_view(request):
    form = AudioUploadForm()
    audios = UploadedAudio.objects.all()

    if request.method == "POST":
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio_obj = form.save(commit=False)
            audio_obj.save()

            messages.info(request, "Audio uploaded. Generating scenes, this may take a moment...")

            audio_path = audio_obj.audio_file.path

            # 1) SCENE GENERATION
            scenes = generate_scenes(audio_path)

            messages.info(request, "Scenes generated. Creating images for each scene...")

            # 2) IMAGE GENERATION
            img_paths = generate_images(scenes, output_dir="pipeline_images")

            # 3) VIDEO GENERATION
            output_path = os.path.join(
                settings.MEDIA_ROOT,
                f"videos/{audio_obj.id}.mp4"
            )
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            if img_paths and len(img_paths) > 0:
                messages.info(request, "Images ready. Rendering video, this can take a bit longer...")

                final_path = create_video(img_paths, audio_path, output_path)

                if final_path:
                    audio_obj.video_file = str(final_path).replace(
                        settings.MEDIA_ROOT + "\\", ""
                    )
                    audio_obj.save()

                    messages.success(request, "Video is ready! Redirecting to result page...")
                    return redirect("result", audio_id=audio_obj.id)

                else:
                    messages.error(request, "Failed to create video. Please try again.")

            else:
                messages.error(request, "Failed to generate images. Please try with another audio file.")

    return render(request, "dashboard.html", {
        "form": form,
        "audios": audios,
    })


def result_view(request, audio_id):
    audio = get_object_or_404(UploadedAudio, id=audio_id)
    return render(request, "result.html", {"audio": audio})
