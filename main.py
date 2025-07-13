import argparse, os, tempfile, shutil
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from gtts import gTTS
import yt_dlp

def download_video(url, output_dir):
    """Download remote video using yt-dlp and return local file path."""
    ydl_opts = {
        'format': 'mp4',
        'quiet': True,
        'outtmpl': os.path.join(output_dir, '%(id)s.%(ext)s')
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

def generate_voice(text, output_file, lang='en'):
    """Generate TTS voice-over as MP3 using gTTS."""
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)

def create_reel(clips, audio_path, output_file):
    """Concatenate video clips and overlay the voice-over."""
    video_clips = [VideoFileClip(c) for c in clips]
    final_clip = concatenate_videoclips(video_clips, method='compose')
    audio_clip = AudioFileClip(audio_path).set_duration(final_clip.duration)
    final_clip = final_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

def main():
    parser = argparse.ArgumentParser(description='AI Reel Generator')
    parser.add_argument('--text', required=True, help='Text for voice‑over')
    parser.add_argument('--videos', nargs='+', required=True, help='Local paths or URLs to video files')
    parser.add_argument('--lang', default='en', help='Voice language (e.g., en, ms, id)')
    parser.add_argument('--output', default='output_reel.mp4', help='Output video filename')
    args = parser.parse_args()

    tempdir = tempfile.mkdtemp(prefix='reelgen_')
    processed_clips = []

    # Prepare video clips
    for vid in args.videos:
        if vid.startswith('http'):
            print(f'Downloading {vid} ...')
            file_path = download_video(vid, tempdir)
        else:
            file_path = os.path.abspath(vid)
        processed_clips.append(file_path)

    # Generate voice‑over
    voice_path = os.path.join(tempdir, 'voice.mp3')
    print('Generating voice‑over ...')
    generate_voice(args.text, voice_path, lang=args.lang)

    # Create final reel
    print('Creating final reel ...')
    create_reel(processed_clips, voice_path, args.output)
    print(f'Done! Reel saved to {args.output}')

    # Cleanup temp
    shutil.rmtree(tempdir)

if __name__ == '__main__':
    main()


