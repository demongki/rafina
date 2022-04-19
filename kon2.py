import asyncio
from aiogram import Bot, Dispatcher, types

api = "5353214002:AAFmkt5I6z2iBStUIHGDZV7y8OjhTAtpDuI"

async def tolong(serah: types.Message):    
    await serah.answer(
    f"Selamat Datang {serah.from_user.get_mention(as_html=True)}, Silahkan memilih fitur\n menu bot : \n• /nuliskiri \n• /nuliskanan \n• /foliokiri \n• /foliokanan",
    parse_mode=types.ParseMode.HTML,)

async def nulis_kiri(pesan: types.Message):
	tulisan = pesan.text.replace('/nuliskiri', '')
	await pesan.answer_photo(types.InputFile.from_url(f"https://api.dapuhy.xyz/api/maker/nuliskiri?text={tulisan}&apikey=risenqpi"))

async def nulis_kanan(pesan: types.Message):	
	tulisann = pesan.text.replace('/nuliskanan', '')
	await pesan.answer_photo(types.InputFile.from_url(f"https://api.dapuhy.xyz/api/maker/nuliskanan?text={tulisann}&apikey=risenqpi"))

async def folio_kiri(pesan: types.Message):
	tulisan = pesan.text.replace('/foliokiri', '')
	await pesan.answer_photo(types.InputFile.from_url(f"https://api.dapuhy.xyz/api/maker/foliokiri?text={tulisan}&apikey=risenqpi"))
	
async def folio_kanan(pesan: types.Message):
	tulisan = pesan.text.replace('/foliokanan', '')
	await pesan.answer_photo(types.InputFile.from_url(f"https://api.dapuhy.xyz/api/maker/foliokanan?text={tulisan}&apikey=risenqpi"))



async def main():
	print("Bot Sedang Berjalan ...")
	bot = Bot(token=api)
	try:
		disp = Dispatcher(bot=bot)
		disp.register_message_handler(tolong, commands={"start"})
		disp.register_message_handler(nulis_kiri, commands="nuliskiri")
		disp.register_message_handler(nulis_kanan, commands="nuliskanan")
		disp.register_message_handler(folio_kiri, commands="foliokiri")
		disp.register_message_handler(folio_kanan, commands="foliokanan")
		await disp.start_polling()
	finally:
		await bot.close()

if __name__ == "__main__":
	try:
		while(True):
			asyncio.run(main())
	except (InterruptedError, KeyboardInterrupt, KeyError, TypeError, IOError, AssertionError, AttributeError, ArithmeticError, BlockingIOError, BrokenPipeError, BufferError, ChildProcessError, ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, DeprecationWarning, EnvironmentError, EOFError, FileExistsError, FileNotFoundError, FloatingPointError, GeneratorExit, ImportError, IndentationError, IndexError, IsADirectoryError, LookupError, MemoryError, ModuleNotFoundError, NameError, NotADirectoryError, NotImplementedError, OSError, OverflowError, PermissionError, ProcessLookupError, RecursionError, ReferenceError, RuntimeError, SyntaxError, SystemError, TabError, TimeoutError, UnboundLocalError, UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError, ValueError, ZeroDivisionError):
		if KeyboardInterrupt:
			print(f"Mohon bersabar sedang menutup bot :')\n\nNote:\t{KeyboardInterrupt}")
			sleep(1.5)
			exit()
		elif TypeError:
			print(f"Terjadi kesalahan dalam mengetik!\nSilahkan baca ulang dengan teliti!\n\nError:\t{TypeError}")
		else:
			print("Malez ngetik njur jadi errornya segini dlu :v")



