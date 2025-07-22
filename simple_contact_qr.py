#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
דוגמה פשוטה ומהירה ליצירת QR code לאיש קשר
"""

import qrcode

def create_simple_contact_qr(name, phone, email=None, filename="my_contact.png"):
    """
    יוצר QR code פשוט עבור איש קשר
    
    Args:
        name (str): שם מלא
        phone (str): מספר טלפון
        email (str, optional): אימייל
        filename (str): שם הקובץ לשמירה
    """
    # יצירת vCard פשוט
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}"""
    
    if email:
        vcard += f"\nEMAIL:{email}"
    
    vcard += "\nEND:VCARD"
    
    # יצירת QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(vcard)
    qr.make(fit=True)
    
    # יצירת תמונה ושמירה
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    
    print(f"QR Code נוצר בהצלחה: {filename}")
    print("סרוק את הקוד עם הטלפון כדי להוסיף את פרטי איש הקשר!")

if __name__ == "__main__":
    # **החלף את הפרטים הבאים בפרטים שלך:**
    
    name = "השם שלך"  # החלף בשם שלך
    phone = "+972-50-1234567"  # החלף במספר הטלפון שלך
    email = "your.email@example.com"  # החלף באימייל שלך (או השאר None)
    
    create_simple_contact_qr(name, phone, email, "my_contact_qr.png")