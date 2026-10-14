import os
import django
from io import BytesIO

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from django.core.files.base import ContentFile
from store.models import Category, Product
from PIL import Image, ImageDraw, ImageFont

# -----------------------------------
# Зураг үүсгэх функц
# -----------------------------------
def create_placeholder_image(product_name):
    width, height = 800, 800
    bg_color = (240, 245, 255)
    text_color = (30, 60, 120)

    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    # Гарчиг
    try:
        font = ImageFont.truetype("arial.ttf", 42)
        small_font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Дээд талын жижиг текст
    top_text = "Online Shop"
    top_bbox = draw.textbbox((0, 0), top_text, font=small_font)
    top_w = top_bbox[2] - top_bbox[0]
    draw.text(((width - top_w) / 2, 120), top_text, fill=text_color, font=small_font)

    # Гол бүтээгдэхүүний нэр
    lines = []
    words = product_name.split()
    line = ""

    for word in words:
        test_line = f"{line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        test_width = bbox[2] - bbox[0]

        if test_width < 550:
            line = test_line
        else:
            lines.append(line)
            line = word

    if line:
        lines.append(line)

    total_text_height = len(lines) * 60
    start_y = (height - total_text_height) / 2

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_w = bbox[2] - bbox[0]
        draw.text(((width - text_w) / 2, start_y + i * 60), line, fill=text_color, font=font)

    # Доод талын жижиг тэмдэг
    bottom_text = "Product Image"
    bottom_bbox = draw.textbbox((0, 0), bottom_text, font=small_font)
    bottom_w = bottom_bbox[2] - bottom_bbox[0]
    draw.text(((width - bottom_w) / 2, 650), bottom_text, fill=(100, 100, 100), font=small_font)

    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()

# -----------------------------------
# Category-ууд
# -----------------------------------
categories = [
    ("Electronics", "electronics"),
    ("Fashion", "fashion"),
    ("Shoes", "shoes"),
    ("Sports", "sports"),
    ("Accessories", "accessories"),
]

for name, slug in categories:
    Category.objects.update_or_create(
        slug=slug,
        defaults={
            "category_name": name,
            "description": f"{name} бүтээгдэхүүнүүд"
        }
    )

# -----------------------------------
# Шинээр нэмэх 10 бараа
# -----------------------------------
products = [
    ("MacBook Air M4", "macbook-air-m4", 6200000, 6, "Electronics",
     "Apple-ийн хөнгөн, хурдан, өндөр үзүүлэлттэй зөөврийн компьютер."),

    ("iPad Pro 13", "ipad-pro-13", 4100000, 9, "Electronics",
     "Том дэлгэцтэй, бүтээлч ажилд тохиромжтой таблет."),

    ("Sony Headset", "sony-headset", 390000, 11, "Accessories",
     "Дуу чимээ тусгаарлагчтай чанартай чихэвч."),

    ("Leather Wallet", "leather-wallet", 85000, 16, "Accessories",
     "Өдөр тутам хэрэглэх арьсан түрийвч."),

    ("Running Shoes", "running-shoes", 320000, 13, "Shoes",
     "Гүйлт болон фитнест зориулсан хөнгөн пүүз."),

    ("Puma Sneakers", "puma-sneakers", 280000, 7, "Shoes",
     "Загварлаг, эвтэйхэн өдөр тутмын пүүз."),

    ("Fitness T-Shirt", "fitness-tshirt", 99000, 20, "Fashion",
     "Спорт дасгалд өмсөх амьсгалдаг материалтай футболк."),

    ("Denim Jacket", "denim-jacket", 210000, 8, "Fashion",
     "Сонгодог загварын жинсэн хүрэм."),

    ("Tennis Racket", "tennis-racket", 260000, 5, "Sports",
     "Теннисний бэлтгэл, тоглолтод зориулсан ракет."),

    ("Yoga Mat", "yoga-mat", 75000, 14, "Sports",
     "Йога болон сунгалтын дасгалд зориулсан дэвсгэр."),
]

for name, slug, price, stock, category_name, description in products:
    category = Category.objects.get(category_name=category_name)

    product, created = Product.objects.update_or_create(
        slug=slug,
        defaults={
            "product_name": name,
            "price": price,
            "stock": stock,
            "category": category,
            "description": description,
            "is_available": True,
        }
    )

    # Хэрэв зураг байхгүй бол автоматаар placeholder зураг үүсгэнэ
    if not product.images:
        image_data = create_placeholder_image(name)
        filename = f"{slug}.png"
        product.images.save(filename, ContentFile(image_data), save=True)

    print(f'{"CREATED" if created else "UPDATED"}: {name}')

print("\nАмжилттай! 10 шинэ бараа зурагтайгаа нэмэгдлээ.")