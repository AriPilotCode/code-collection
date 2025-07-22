#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
גרסה אינטרקטיבית ליצירת QR code לאיש קשר
המשתמש יכול להזין את הפרטים שלו דרך הקונסול
"""

import qrcode

def get_user_input():
    """מקבל פרטים מהמשתמש"""
    print("=== יוצר QR Code לפרטי איש קשר ===")
    print()
    
    name = input("הכנס את השם המלא שלך: ")
    phone = input("הכנס את מספר הטלפון (בפורמט +972-XX-XXXXXXX): ")
    
    email = input("הכנס כתובת אימייל (אופציונלי, לחץ Enter לדילוג): ").strip()
    if not email:
        email = None
    
    organization = input("הכנס שם החברה/ארגון (אופציונלי, לחץ Enter לדילוג): ").strip()
    if not organization:
        organization = None
    
    website = input("הכנס כתובת אתר (אופציונלי, לחץ Enter לדילוג): ").strip()
    if not website:
        website = None
    
    return {
        'name': name,
        'phone': phone,
        'email': email,
        'organization': organization,
        'website': website
    }

def create_contact_qr(contact_info):
    """יוצר QR code מפרטי איש הקשר"""
    # יצירת vCard
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{contact_info['name']}\nTEL:{contact_info['phone']}"
    
    if contact_info['email']:
        vcard += f"\nEMAIL:{contact_info['email']}"
    
    if contact_info['organization']:
        vcard += f"\nORG:{contact_info['organization']}"
    
    if contact_info['website']:
        vcard += f"\nURL:{contact_info['website']}"
    
    vcard += "\nEND:VCARD"
    
    print("\nvCard שנוצר:")
    print("-" * 40)
    print(vcard)
    print("-" * 40)
    
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
    
    # שם הקובץ מבוסס על השם
    safe_name = contact_info['name'].replace(" ", "_").replace("/", "_")
    filename = f"contact_{safe_name}.png"
    
    img.save(filename)
    
    print(f"\n✅ QR Code נוצר בהצלחה!")
    print(f"📁 נשמר בקובץ: {filename}")
    print("\n📱 איך להשתמש:")
    print("1. פתח את אפליקציית המצלמה בטלפון")
    print("2. כוון את המצלמה על ה-QR code")
    print("3. לחץ על ההתראה שמופיעה")
    print("4. בחר 'הוסף לאנשי קשר'")
    print("\n🎉 זהו! פרטי איש הקשר יתווספו לטלפון!")

def main():
    """פונקציה ראשית"""
    try:
        contact_info = get_user_input()
        create_contact_qr(contact_info)
    except KeyboardInterrupt:
        print("\n\nביטול הפעולה.")
    except Exception as e:
        print(f"\nשגיאה: {e}")

if __name__ == "__main__":
    main()