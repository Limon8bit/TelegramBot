import telebot
import requests
# import speech_recognition as sr
# from pydub import AudioSegment


token = 'YOUR TELEGRAM TOKEN'
bot = telebot.TeleBot(token)
print('Бот запущен')

@bot.message_handler(content_types=['audio'])
def repeat_all_message(message):
    print('какой-то аудио файл')
    file_info = bot.get_file(message.audio.file_id)
    file = requests.get(f'https://api.telegram.org/file/bot{token}/{file_info.file_path}')
    with open(f'./media_files/{file_info.file_path}', 'x') as f:
        f.close()
    with open(f'./media_files/{file_info.file_path}','wb') as f:
        f.write(file.content)
    # sound = AudioSegment.from_mp3('./media_files/music/file_17.mp3')
    # with open(f"{file_info}.wav", 'x') as file:
    #     file.close()
    # sound.export(f"{file_info}.wav", format="wav")
    # AUDIO_FILE = f"{file_info}.wav"

    # r = sr.Recognizer()
    # with sr.AudioFile(AUDIO_FILE) as source:
    #     audio = r.record(source)  # read the entire audio file
    #     print("Transcription: " + r.recognize_google(audio))


if __name__ == '__main__':
    bot.polling(none_stop=True)

