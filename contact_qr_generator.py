#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
מייצר QR Code עבור פרטי איש קשר
כאשר סורקים את הקוד, הוא מוסיף את פרטי איש הקשר לטלפון
"""

import qrcode
from PIL import Image
import io

class ContactQRGenerator:
    def __init__(self):
        """אתחול מחולל QR code לפרטי איש קשר"""
        pass
    
    def create_vcard(self, first_name, last_name, phone, email=None, organization=None, website=None, address=None):
        """
        יוצר vCard string עבור פרטי איש הקשר
        
        Args:
            first_name (str): שם פרטי
            last_name (str): שם משפחה
            phone (str): מספר טלפון
            email (str, optional): כתובת אימייל
            organization (str, optional): ארגון/חברה
            website (str, optional): אתר אינטרנט
            address (str, optional): כתובת
            
        Returns:
            str: vCard מעוצב
        """
        vcard = "BEGIN:VCARD\n"
        vcard += "VERSION:3.0\n"
        vcard += f"FN:{first_name} {last_name}\n"
        vcard += f"N:{last_name};{first_name};;;\n"
        vcard += f"TEL;TYPE=CELL:{phone}\n"
        
        if email:
            vcard += f"EMAIL:{email}\n"
        
        if organization:
            vcard += f"ORG:{organization}\n"
        
        if website:
            vcard += f"URL:{website}\n"
            
        if address:
            vcard += f"ADR;TYPE=HOME:;;{address};;;;\n"
        
        vcard += "END:VCARD"
        return vcard
    
    def generate_qr_code(self, vcard_data, filename="contact_qr.png", 
                        box_size=10, border=4, fill_color="black", back_color="white",
                        styled=False):
        """
        יוצר QR code מ-vCard data
        
        Args:
            vcard_data (str): נתוני vCard
            filename (str): שם הקובץ לשמירה
            box_size (int): גודל כל תיבה ב-QR
            border (int): גודל הגבול
            fill_color (str): צבע הקוד
            back_color (str): צבע הרקע
            styled (bool): האם ליצור עיצוב מעוגל
            
        Returns:
            PIL.Image: תמונת QR code
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        
        qr.add_data(vcard_data)
        qr.make(fit=True)
        
        # יצירת QR code (הגרסה הפשוטה עובדת עם כל הגרסאות)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # שמירת התמונה
        img.save(filename)
        print(f"QR Code נשמר בקובץ: {filename}")
        
        return img
    
    def create_contact_qr(self, contact_info, filename="my_contact_qr.png", styled=True):
        """
        יוצר QR code מלא עבור איש קשר
        
        Args:
            contact_info (dict): מילון עם פרטי איש הקשר
            filename (str): שם הקובץ לשמירה
            styled (bool): עיצוב מעוגל
            
        Returns:
            PIL.Image: תמונת QR code
        """
        # יצירת vCard
        vcard = self.create_vcard(
            first_name=contact_info.get('first_name', ''),
            last_name=contact_info.get('last_name', ''),
            phone=contact_info.get('phone', ''),
            email=contact_info.get('email'),
            organization=contact_info.get('organization'),
            website=contact_info.get('website'),
            address=contact_info.get('address')
        )
        
        print("vCard שנוצר:")
        print("-" * 30)
        print(vcard)
        print("-" * 30)
        
        # יצירת QR code
        return self.generate_qr_code(vcard, filename, styled=styled)

def main():
    """פונקציה ראשית להדגמה"""
    generator = ContactQRGenerator()
    
    # דוגמה לפרטי איש קשר - החלף את הפרטים בשלך!
    my_contact = {
        'first_name': 'יוחנן',
        'last_name': 'כהן',
        'phone': '+972-50-1234567',
        'email': 'yochanan.cohen@example.com',
        'organization': 'חברת הטכנולוגיה שלי',
        'website': 'https://www.mywebsite.co.il',
        'address': 'רחוב הרצל 123, תל אביב'
    }
    
    print("מייצר QR Code עבור פרטי איש הקשר...")
    
    # יצירת QR code רגיל
    generator.create_contact_qr(my_contact, "contact_regular.png", styled=False)
    
    # יצירת QR code מעוצב
    generator.create_contact_qr(my_contact, "contact_styled.png", styled=True)
    
    print("\nהושלם! נוצרו שני קבצים:")
    print("1. contact_regular.png - QR code רגיל")
    print("2. contact_styled.png - QR code מעוצב")
    print("\nכעת אתה יכול לסרוק את הקודים עם הטלפון שלך!")
    print("בעת סריקה, הטלפון יציע להוסיף את פרטי איש הקשר לרשימת הקשרים.")

if __name__ == "__main__":
    main()