from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# Buat presentasi baru
prs = Presentation()

# Atur slide ke ukuran standar (10 x 7,5 inch)
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Slide 1: Title Slide
slide_layout = prs.slide_layouts[6]  # Blank layout (tanpa placeholder)
slide = prs.slides.add_slide(slide_layout)

# Tambahkan title
title_box = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(2))
tf = title_box.text_frame
tf.text = "Mini Program Kalkulator"
tf.paragraphs[0].font.size = Pt(44)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)
tf.paragraphs[0].alignment = PP_ALIGN.CENTER

# Tambahkan subtitle
subtitle_box = slide.shapes.add_textbox(Inches(1), Inches(4), Inches(8), Inches(2))
tf = subtitle_box.text_frame
tf.text = "Oleh: [Muhammad Azfa Eka Satria]\nTanggal: [14 Oktober 2026]\nDeskripsi: Presentasi projek kalkulator sederhana dengan Python dan unit testing"
tf.paragraphs[0].font.size = Pt(16)
tf.paragraphs[0].font.color.rgb = RGBColor(64, 64, 64)
tf.paragraphs[0].alignment = PP_ALIGN.CENTER

# Slide 2: Pendahuluan
slide = prs.slides.add_slide(slide_layout)

# Tambahkan title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(1))
tf = title_box.text_frame
tf.text = "Pendahuluan"
tf.paragraphs[0].font.size = Pt(36)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

# Tambahkan konten
content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(5))
tf = content_box.text_frame
tf.word_wrap = True

# Tujuan Projek
p = tf.paragraphs[0]
p.text = "Tujuan Projek:"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• Membuat kalkulator sederhana dengan Python"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = "• Memastikan semua fungsi bekerja dengan benar melalui unit testing (4 fungsi diuji)"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = ""
p.font.size = Pt(12)  # Spacer

# Fitur Utama
p = tf.add_paragraph()
p.text = "Fitur Utama:"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• Operasi: Tambah, Kurangi, Kali, Bagi"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = "• Unit test 4 fungsi (tambah, kurangi, kali, bagi)"
p.font.size = Pt(16)
p.level = 1

# Slide 3: Struktur Program
slide = prs.slides.add_slide(slide_layout)

# Tambahkan title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(1))
tf = title_box.text_frame
tf.text = "Struktur Program"
tf.paragraphs[0].font.size = Pt(36)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

# Tambahkan konten
content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(5))
tf = content_box.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "File dalam Repository:"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• kalkulator.py: Fungsi inti kalkulator"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = "• test_kalkulator.py: Unit test"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = "• main.py: Antarmuka pengguna"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = ""
p.font.size = Pt(12)  # Spacer

p = tf.add_paragraph()
p.text = "Class Kalkulator:"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• Method: tambah, kurangi, kali, bagi"
p.font.size = Pt(16)
p.level = 1

# Slide 4: Test Case Design
slide = prs.slides.add_slide(slide_layout)

# Tambahkan title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(1))
tf = title_box.text_frame
tf.text = "Test Case Design"
tf.paragraphs[0].font.size = Pt(36)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

# Buat tabel untuk test case
rows, cols = 7, 6
left, top, width, height = Inches(0.5), Inches(1.5), Inches(9), Inches(4.2)
table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
table = table_shape.table

# Set lebar kolom
table.columns[0].width = Inches(0.8)
table.columns[1].width = Inches(1.5)
table.columns[2].width = Inches(2.5)
table.columns[3].width = Inches(1.5)
table.columns[4].width = Inches(1.5)
table.columns[5].width = Inches(1.2)

# Isi header
headers = ["No", "Test Case ID", "Deskripsi", "Input", "Expected Output", "Status"]
for i, header in enumerate(headers):
    cell = table.cell(0, i)
    cell.text = header
    cell.fill.solid()
    cell.fill.fore_color.rgb = RGBColor(70, 130, 180)
    for paragraph in cell.text_frame.paragraphs:
        paragraph.font.bold = True
        paragraph.font.color.rgb = RGBColor(255, 255, 255)
        paragraph.font.size = Pt(12)
        paragraph.alignment = PP_ALIGN.CENTER

# Isi data
data = [
    ["1", "TC_ADD_001", " tambah dua angka positif", "5, 3", "8", "Pass"],
    ["2", "TC_ADD_002", " tambah angka negatif", "-2, 4", "2", "Pass"],
    ["3", "TC_KUR_001", " kurangi dua angka positif", "10, 4", "6", "Pass"],
    ["4", "TC_KUR_002", " kurangi angka lebih kecil", "5, 10", "-5", "Pass"],
    ["5", "TC_KAL_001", " kali dua angka positif", "3, 4", "12", "Pass"],
    ["6", "TC_BAG_001", " bagi dengan nol", "10, 0", "Error", "Pass"]
]

for row_idx, row_data in enumerate(data, start=1):
    for col_idx, cell_value in enumerate(row_data):
        cell = table.cell(row_idx, col_idx)
        cell.text = cell_value
        for paragraph in cell.text_frame.paragraphs:
            paragraph.font.size = Pt(11)
            paragraph.font.color.rgb = RGBColor(0, 0, 0)
            if col_idx == 0 or col_idx == 5:  # Center align for No and Status
                paragraph.alignment = PP_ALIGN.CENTER

# Tambahkan penjelasan
explanation_box = slide.shapes.add_textbox(Inches(0.5), Inches(5.9), Inches(9), Inches(1.5))
tf = explanation_box.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Penjelasan:"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• Test case dirancang untuk memvalidasi setiap operasi"
p.font.size = Pt(14)
p.level = 1

p = tf.add_paragraph()
p.text = "• Input dan expected output diuji secara otomatis"
p.font.size = Pt(14)
p.level = 1

# Slide 5: Unit Test Implementation
slide = prs.slides.add_slide(slide_layout)

# Tambahkan title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(1))
tf = title_box.text_frame
tf.text = "Unit Test Implementation"
tf.paragraphs[0].font.size = Pt(36)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

# Tambahkan konten
content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(0.8))
tf = content_box.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Contoh Kode (Python):"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

# Buat code box
code_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.4), Inches(9), Inches(2.3))
tf = code_box.text_frame
tf.word_wrap = True

code_text = """import unittest
from kalkulator import Kalkulator

class TestKalkulator(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(Kalkulator.tambah(5, 3), 8)

    def test_kurangi(self):
        self.assertEqual(Kalkulator.kurangi(10, 4), 6)

    def test_kali(self):
        self.assertEqual(Kalkulator.kali(3, 4), 12)

    def test_bagi(self):
        self.assertEqual(Kalkulator.bagi(10, 2), 5)
        with self.assertRaises(ValueError):
            Kalkulator.bagi(10, 0)"""

p = tf.paragraphs[0]
p.text = code_text
p.font.name = 'Courier New'
p.font.size = Pt(10)
p.font.color.rgb = RGBColor(0, 0, 0)

# Tambahkan penjelasan
explanation_box = slide.shapes.add_textbox(Inches(0.5), Inches(5), Inches(9), Inches(2))
tf = explanation_box.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Penjelasan:"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• Meng menggunakan framework unittest"
p.font.size = Pt(14)
p.level = 1

p = tf.add_paragraph()
p.text = "• Setiap method test memvalidasi satu fungsi"
p.font.size = Pt(14)
p.level = 1

# Slide 6: Hasil Unit Test
slide = prs.slides.add_slide(slide_layout)

# Tambahkan title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(1))
tf = title_box.text_frame
tf.text = "Hasil Unit Test"
tf.paragraphs[0].font.size = Pt(36)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

# Tambahkan konten
content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(0.8))
tf = content_box.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Output Terminal:"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

# Buat output box
output_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.4), Inches(9), Inches(2))
tf = output_box.text_frame
tf.word_wrap = True

output_text = """.....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK"""

p = tf.paragraphs[0]
p.text = output_text
p.font.name = 'Courier New'
p.font.size = Pt(12)
p.font.color.rgb = RGBColor(0, 0, 0)

# Tambahkan kesimpulan
conclusion_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.5), Inches(9), Inches(2.5))
tf = conclusion_box.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Kesimpulan:"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• Semua test case PASS"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = "• Fungsi kalkulator bekerja dengan benar"
p.font.size = Pt(16)
p.level = 1

# Slide 7: Kesimpulan
slide = prs.slides.add_slide(slide_layout)

# Tambahkan title
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(1))
tf = title_box.text_frame
tf.text = "Kesimpulan"
tf.paragraphs[0].font.size = Pt(36)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

# Tambahkan konten
content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(5))
tf = content_box.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Hasil Projek:"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• Mini program kalkulator selesai dibuat"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = "• Unit test memastikan fungsi akurat"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = ""
p.font.size = Pt(12)  # Spacer

p = tf.add_paragraph()
p.text = "Saran Pengembangan:"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)

p = tf.add_paragraph()
p.text = "• Tambahkan fitur seperti operasi pangkat atau akar"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = "• Buat antarmuka grafis (GUI)"
p.font.size = Pt(16)
p.level = 1

p = tf.add_paragraph()
p.text = ""
p.font.size = Pt(12)  # Spacer

p = tf.add_paragraph()
p.text = "Terima Kasih!"
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 51, 102)
p.alignment = PP_ALIGN.CENTER

p = tf.add_paragraph()
p.text = "Q&A"
p.font.size = Pt(20)
p.font.bold = True
p.font.color.rgb = RGBColor(0, 0, 0)
p.alignment = PP_ALIGN.CENTER

# Simpan presentasi
prs.save('presentasi_kalkulator.pptx')
print("File PowerPoint 'presentasi_kalkulator.pptx' telah dibuat!")
print("Silakan jalankan script ini di Python untuk menghasilkan file PowerPoint.")