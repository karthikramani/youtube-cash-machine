from PIL import Image, ImageDraw, ImageFont
import os

# Slide texts
texts = [
    "WHAT IF I TOLD YOU...",
    "CHANNELS EARNING\n$5K-50K/MONTH",
    "WHY MOST PEOPLE\nNEVER START",
    "THE EQUIPMENT\nPROBLEM",
    "THERE'S A\nDIFFERENT WAY",
    "THE A.I.R.\nFRAMEWORK™",
    "THE 30-MINUTE\nSYSTEM",
    "IS THERE\nDEMAND?",
    "WHAT YOU'LL\nLEARN",
    "6 BONUSES\nINCLUDED",
    "THE 90-DAY\nTIMELINE",
    "$297\nONE-TIME",
    "TWO\nCHOICES",
    "IMAGINE 90 DAYS\nFROM NOW",
    "CLICK THE BUTTON\nBELOW"
]

os.makedirs("slides", exist_ok=True)

for i, text in enumerate(texts, 1):
    # Create image
    img = Image.new('RGB', (1920, 1080), color=(10, 14, 26))
    draw = ImageDraw.Draw(img)
    
    # Use default font (large size)
    try:
        font = ImageFont.truetype("arial.ttf", 120)
    except:
        font = ImageFont.load_default()
    
    # Get text bbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center text
    x = (1920 - text_width) / 2
    y = (1080 - text_height) / 2
    
    # Draw text
    draw.text((x, y), text, fill='white', font=font, align='center')
    
    # Save
    filename = f"slides/slide-{i:02d}.png"
    img.save(filename)
    print(f"✅ Slide {i} created")

print(f"\n✅ All 15 slides created!")
