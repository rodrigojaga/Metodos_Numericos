import pdfkit
from objResultado import NRMResultado, NRSimpleResultado
from datetime import datetime

nombreDocumento = "0900-22-1379_Rodrigo_Galindo_P1"
codigo_del_documento = ""


css_style = """
<style>
table {
   border-collapse: collapse;
    width: 100%;
}
th, td{
    padding: 0;
    text-align: center;
}
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
thead th{
    background-color: #f2f2f2;
    font-weight: bold;
}
td{
    style="font-size: 1px;"
}
.encabezado {
   background-color: #ccc;
}
.tabla {
    background-color: #fff;
}
</style>
<br>
"""


def crearTabla(ecuacionCuadratica: bool, biseccion: bool, NRSimple: bool, NRModificado: bool, lista_para_pdf):
    if ecuacionCuadratica:
        tabla_ecuacion_cuadratica = """
        <br>  
        <div>
        <h5>cuadratica</h5>      
        <table border="1" style="border-collapse: collapse; width: 100%;" class = "tabla">
        <thead>
        <tr>
            <th class ="encabezado">     Coeficiente a     </th>
            <th class ="encabezado">     Coeficiente b     </th>
            <th class ="encabezado">     Coeficiente c     </th>
            <th class ="encabezado">     X1     </th>
            <th class ="encabezado">     X2     </th>
        </tr>
        </thead>
        <br>
        """
        insertarDatosEcuacionCuadratica(lista_para_pdf, tabla_ecuacion_cuadratica)
    if biseccion:
        tabla_biseccion = """
        <br> 
        <div>
        <h5>biseccion</h5>       
        <table border="1" style="border-collapse: collapse; width: 100%;" class = "tabla">
        <thead>
        <tr>
            <th class ="encabezado">     i     </th>
            <th class ="encabezado">     Xl     </th>
            <th class ="encabezado">     f(Xl)     </th>
            <th class ="encabezado">     Xu     </th>
            <th class ="encabezado">     f(Xu)     </th>
            <th class ="encabezado">     Xr     </th>
            <th class ="encabezado">     f(Xr)     </th>
            <th class ="encabezado">     E     </th>
        </tr>
        </thead>
        <br>
        """
        insertarDatosBiseccion(lista_para_pdf, tabla_biseccion)
    if NRSimple:
        tabla_newton_simple = """
        <br>
        <div>
        <h5>newton-rapson simple</h5>
        <table border="1" style="border-collapse: collapse; width: 100%;" class = "tabla">
        <thead>
        <tr>
            <th class ="encabezado">     i     </th>
            <th class ="encabezado">     Xi     </th>
            <th class ="encabezado">     f(Xi)     </th>
            <th class ="encabezado">     f'(Xi)     </th>
            <th class ="encabezado">     Xi+1     </th>
            <th class ="encabezado">     E     </th>
        </tr>
        </thead>
        <br>
        """
        insertarDatosNRSimple(lista_para_pdf, tabla_newton_simple)
    if NRModificado:
        tabla_newton_mejorado = """
        <br>
        <div>
        <h5>newton - rapson modificado</h5>
        <table border="1" style="border-collapse: collapse; width: 100%;" class = "tabla">
        <thead>
        <tr>
            <th class ="encabezado">     i     </th>
            <th class ="encabezado">     Xi     </th>
            <th class ="encabezado">     f(Xi)     </th>
            <th class ="encabezado">     f'(Xi)     </th>
            <th class ="encabezado">     f''(Xi)     </th>
            <th class ="encabezado">     Xi+1     </th>
            <th class ="encabezado">     E     </th>
        </tr>
        </thead>
        <br>
        """
        insertarDatosNRModificado(lista_para_pdf, tabla_newton_mejorado)


def insertarDatosEcuacionCuadratica(lista_para_pdf, tabla_encabezado):
    global codigo_del_documento
    tabla_ecuacion_cuadratica = ""
    for iteracion in lista_para_pdf:
        tabla_ecuacion_cuadratica += f"""
    <tr>
        <td>{iteracion.a}</td>
        <td>{iteracion.b}</td>
        <td>{iteracion.c}</td>
        <td>{iteracion.X1}</td>
        <td>{iteracion.X2}</td>
    </tr>
    </div>
    """
    codigo_del_documento += tabla_encabezado + tabla_ecuacion_cuadratica


def insertarDatosBiseccion(lista_para_pdf, tabla_encabezado):
    global codigo_del_documento
    tabla_biseccion = ""
    for iteracion in lista_para_pdf:
        tabla_biseccion += f"""
    <tr>
        <td>{iteracion.i}</td>
        <td>{iteracion.Xl}</td>
        <td>{iteracion.fXl}</td>
        <td>{iteracion.Xu}</td>
        <td>{iteracion.fXu}</td>
        <td>{iteracion.Xr}</td>
        <td>{iteracion.fXr}</td>
        <td>{iteracion.error}</td>
    </tr>
    </div>
    """
    codigo_del_documento += tabla_encabezado + tabla_biseccion

def insertarDatosNRSimple(lista_para_pdf, tabla_encabezado):
    global codigo_del_documento
    tabla_newton_rapson_simple = ""
    for iteracion in lista_para_pdf:
        tabla_newton_rapson_simple += f"""
    <tr>
        <td>{iteracion.i}</td>
        <td>{iteracion.Xi}</td>
        <td>{iteracion.fXi}</td>
        <td>{iteracion.fXiDerivada}</td>
        <td>{iteracion.XiSiguiente}</td>            
        <td>{iteracion.error}</td>
    </tr>
    </div>
        """
    codigo_del_documento += tabla_encabezado + tabla_newton_rapson_simple

def insertarDatosNRModificado(lista_para_pdf, tabla_encabezado):
    global codigo_del_documento
    tabla_newtonR_modificado = ""
    for iteracion in lista_para_pdf:
        tabla_newtonR_modificado += f"""
   <tr>
       <td>{iteracion.i}</td>
       <td>{iteracion.Xi}</td>
       <td>{iteracion.fXi}</td>
       <td>{iteracion.fXiDerivada}</td>
       <td>{iteracion.fXiSegundaDerivada}</td>
       <td>{iteracion.XiSiguiente}</td>            
       <td>{iteracion.error}</td>
   </tr>
   </div>
       """
    codigo_del_documento += tabla_encabezado + tabla_newtonR_modificado


def finalizarPDF():
    global codigo_del_documento, css_style
    try:
        with open(f"{nombreDocumento}.html", "w") as file:
            file.write(css_style + codigo_del_documento)
        exe = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=exe)
        pdfkit.from_file(f"{nombreDocumento}.html", f"{nombreDocumento}.pdf", configuration=config)
        print("Documento Creado")
    except Exception as e:
        print(f"Error al generar PDF: {e}")


