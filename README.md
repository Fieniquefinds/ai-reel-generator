# AI Reel Generator (Windows PC)

Simple command‑line tool to generate social‑media‑style video reels by combining:
1. **One or more video clips** (local files *or* remote URLs, e.g. YouTube/TikTok links)
2. **Text voice‑over** generated on‑the‑fly (gTTS)

## Prerequisites

- **Python 3.10+**
- **FFmpeg** in your PATH (download from https://ffmpeg.org and add `bin` folder to the system PATH)
- Internet connection (gTTS and yt‑dlp both fetch online resources)

## Installation

```bash
# 1. Clone or unzip this folder
cd ai_reel_generator
# 2. Create and activate a virtual environment (recommended)
python -m venv .venv
.\.venv\Scripts\activate   # Windows PowerShell
# 3. Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Example 1: Combine local.mp4 + remote YouTube clip, voice‑over in English
python main.py --text "Welcome to my AI reel demo!" --videos local.mp4 https://www.youtube.com/watch?v=dQw4w9WgXcQ --output my_reel.mp4

# Example 2: Malay voice‑over, multiple local files
python main.py --text "Ini contoh video pendek dengan suara latar." --lang ms --videos clip1.mp4 clip2.mp4 --output demo_reel.mp4
```

**What happens:**
1. Remote URLs are downloaded (mp4) to a temp folder via `yt‑dlp`.
2. `gTTS` converts your `--text` into `voice.mp3` (set `--lang` for language).
3. `moviepy` concatenates all video clips, overlays the voice‑over, and exports a final `mp4`.

## Customising Further

- Replace `gTTS` with **OpenAI TTS**, **ElevenLabs**, or **Azure Speech** if you want higher‑quality voices. Just edit `generate_voice()` in `main.py`.
- Add background music: load an extra `AudioFileClip` and mix it with the voice‑over.
- Insert captions: use `TextClip` from `moviepy` and composite over the video.
- Automate aspect‑ratio conversion: `video.resize(height=1920).crop(x_center, width=1080)` for vertical reels.

## Troubleshooting

- **moviepy errors / FFMPEG not found**: ensure `ffmpeg.exe` is accessible in PATH.
- **gTTS very slow or fails**: it depends on Google TTS service; for offline TTS use `pyttsx3`.
- **yt‑dlp download failed**: some sites block; update yt‑dlp (`python -m pip install -U yt-dlp`).

## License

MIT – do anything, but no warranty.
