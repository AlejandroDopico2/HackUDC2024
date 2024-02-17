import os
import PyPDF2


def read_pdf(path):
    pdf = open(path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdf)
    pageObj = pdfReader.pages[0]
    res = extract_information(pageObj)
    return res

def extract_information(text):
    nombre_empresa = text.split("-")[0]

    numero_factura = text.split('Nº factura:')[1].split('Fecha de emisión:')[0].strip()

    fecha_emision = text.split('Fecha de emisión:')[1].split('Fecha de cargo:')[0].strip()
    fecha_cargo = text.split('Fecha de cargo:')[1].split('Electricidad:')[0].strip()

    total_pagar = text.split('Total\na\npagar')[1].split('\n€')[0].strip()

    direccion_suministro = text.split('Dirección\nsuministro:')[1].split('Nº factura:')[0].replace("\n", " ")

    detalle_costos = text.split('siguiente\ndestino:\n')[1].split("\nEnergía")[0].strip().replace("\n", " ").replace(
        "%", " ").split("  ")

    detalle_costos = list(map(lambda x: float(x.replace(',', '.')), detalle_costos))

    detalle_costos.sort(reverse=True)

    return (f"Nombre de la Empresa: {nombre_empresa}\nNúmero de Factura:{numero_factura}\nFecha de Emisión:{fecha_emision}\nFecha de Cargo:{fecha_cargo}\nTotal a Pagar:{total_pagar} Dirección de Suministro:{direccion_suministro}\n"
            f"Detalle de Costos:\n Energía: {detalle_costos[0]} %\n Alquiler contador: {detalle_costos[1]} %\n Impuestos: {detalle_costos[2]} %\n Cargos: {detalle_costos[3]}\n Peajes: {detalle_costos[4]} %\n\n\n")
