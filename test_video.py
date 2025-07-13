from moviepy.editor import VideoFileClip

try:
    clip = VideoFileClip("klip1.mp4")
    print("✅ Video berjaya dimuatkan!")
    print(f"⏱️ Tempoh: {clip.duration} saat")
except OSError as e:
    print("❌ Gagal membuka fail video.")
    print(e)
except Exception as ex:
    print("❌ Ralat lain berlaku:")
    print(ex)
