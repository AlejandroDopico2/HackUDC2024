import PyPDF2


def extraer_informacion(factura):
    # Nombre de la Empresa
    nombre_empresa = factura.split("-")[0]

    # Número de Factura
    numero_factura = factura.split('Nº factura:')[1].split('Fecha de emisión:')[0].strip()

    # Fecha de Emisión y Fecha de Cargo
    fecha_emision = factura.split('Fecha de emisión:')[1].split('Fecha de cargo:')[0].strip()
    fecha_cargo = factura.split('Fecha de cargo:')[1].split('Electricidad:')[0].strip()

    # Total a Pagar
    total_pagar = factura.split('Total\na\npagar')[1].split('\n€')[0].strip()

    # Dirección de Suministro
    direccion_suministro = factura.split('Dirección\nsuministro:')[1].split('Nº factura:')[0].replace("\n", " ")

    # Detalle de Costos
    detalle_costos = factura.split('siguiente\ndestino:\n')[1].split("\nEnergía")[0].strip().replace("\n", " ").replace(
        "%", " ").split("  ")
    detalle_costos = list(map(lambda x: float(x.replace(',', '.')), detalle_costos))
    detalle_costos.sort(reverse=True)

    # Imprimir la información
    print("Nombre de la Empresa:", nombre_empresa)
    print("Número de Factura:", numero_factura)
    print("Fecha de Emisión:", fecha_emision)
    print("Fecha de Cargo:", fecha_cargo)
    print("Total a Pagar:", total_pagar)
    print("Dirección de Suministro:", direccion_suministro)
    print(f"Detalle de Costos:\n Energía: {detalle_costos[0]}\n Alquiler contador: {detalle_costos[1]}\n Impuestos: {detalle_costos[2]}\n Cargos: {detalle_costos[3]}\n Peajes: {detalle_costos[4]}\n")

    return (nombre_empresa, numero_factura, fecha_emision, fecha_cargo, total_pagar, direccion_suministro)


def read_pdf(path):
    pdf = open(path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdf)
    pageObj = pdfReader.pages[0]

    return pageObj.extract_text()


if __name__ == '__main__':
    content = read_pdf('./bills/factura4.pdf')
    f = open("info.txt", "+w")
    f.write(content)
    info = extraer_informacion(content)
