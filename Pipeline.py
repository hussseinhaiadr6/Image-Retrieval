from Excel_Image_Extractor import Extract_images_from_excel
from Loader import get_similar_images
from Excel_image_writer import write_result_to_excel


Excel_file="C:/Users/HHR6/PycharmProjects/Task3/Gamme ESSENTIELLE - Sanitaires.xlsx"

output_dir=Extract_images_from_excel(Excel_file,"PHOTO","NOM DU PRODUIT")
print("finished extracting images from Excel file")
get_similar_images(output_dir)
write_result_to_excel(Excel_file,10)


