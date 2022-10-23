from winotify import Notification, audio

toast = Notification(
      app_id="Dvpumut Bildirim",
      title="Beni taip et",
      msg="Buraya Tıkla",
      duration="long", #Uyarı süresi
      icon=r"C:\Users\username\OneDrive\Masaüstü\Python dersleri/bildirim.ico" #Bildirim ikonunun dosya konumu 
)

toast.add_actions(label="Tıka",
      launch="https://youtu.be/6QfYNJGfMd8") #Bildirim sesi.
toast.set_audio(audio.Reminder, loop=False) #Eğer True yaparsanız siz kapatana kadar devam eder. 
toast.show()