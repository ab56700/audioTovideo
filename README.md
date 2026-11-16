# Podcast-to-Video Generator

A Python and Django-based web application that transforms audio files into visually engaging videos using AI-generated images.

## Overview

The Podcast-to-Video Generator converts audio files into videos by generating scenes from the audio content, creating relevant images using AI, and combining them with the original audio to produce a final MP4 video.

The application provides a simple web interface where users can upload audio files, generate videos, preview the results, and download the completed videos.

## Features

- **Audio Upload:** Upload audio files through the web interface.
- **AI Scene Generation:** Generate relevant scenes based on the uploaded audio.
- **AI Image Generation:** Create images for individual scenes using Pollinations AI.
- **Video Generation:** Combine generated images and original audio into an MP4 video.
- **Video Preview:** Watch generated videos directly in the application.
- **Download:** Download the final generated video.

## Technologies Used

| Technology | Purpose |

| Python | Core programming language |
| Django | Web framework |
| Pollinations AI | AI image generation |
| MoviePy | Video creation and editing |
| HTML & CSS | Frontend design |
| SQLite | Database |
| NumPy | Numerical operations |

## How It Works

1. Upload an audio file.
2. The application processes the audio and generates relevant scenes.
3. AI generates images corresponding to each scene.
4. MoviePy combines the generated images with the uploaded audio.
5. A final MP4 video is created.
6. Preview and download the generated video.
