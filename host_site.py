import http.server
import socketserver
import socket

# پورت سرور: 8000 (این عدد را برای سایت های بعدی تغییر دهید)
PORT = 8000

# در اینجا مشخص می کنید که چه فایل هایی را می خواهید سرویس دهید.
# اگر این مقدار را خالی بگذارید، محتوای پوشه فعلی (جایی که این فایل اجرا شده) را سرویس می دهد.
Handler = http.server.SimpleHTTPRequestHandler

# تلاش برای پیدا کردن IP محلی سیستم شما برای دسترسی دستگاه های دیگر
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP_ADDRESS = s.getsockname()[0]
    s.close()
except Exception:
    # در صورت عدم موفقیت در یافتن IP شبکه، از IP لوکال هاست استفاده می شود
    IP_ADDRESS = "127.0.0.1" 

print(f"سرور فعال شد! پورت: {PORT}")
print(f"آدرس محلی (Local): http://127.0.0.1:{PORT}")
print(f"آدرس شبکه (Network - برای دستگاه های دیگر): http://{IP_ADDRESS}:{PORT}")

# شروع به سرویس دهی
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # httpd.serve_forever() برنامه را تا زمانی که متوقف نشود، فعال نگه می دارد.
    httpd.serve_forever()