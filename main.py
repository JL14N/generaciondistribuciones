from flask import Flask, request, render_template, redirect, url_for, flash
from generacion_aleatorios import generar_dist_uniforme, generar_dist_exponencial, generar_dist_normal
from histograma import graficar_histograma, guardar_imagen, tabla_frecuencias

app = Flask(__name__)
app.secret_key = 'l0r3m1ps8md0l0rs1t4m3t'

@app.route('/', methods=['GET', 'POST'])
def main_menu():
    if request.method == 'POST':
        distribution = request.form.get('distribution')

        # Construct query parameters
        params = {
            'cantidad': int(request.form['cantidad']),
            'visualizar': 'visualizar' in request.form,
            'intervalos': int(request.form['intervalos']),
        }
        
        if distribution == 'uniforme':
            a = float(request.form['a'])
            b = float(request.form['b'])
            a > b and flash('Se han invertido los límites superior e inferior', 'info')
            params.update({'a': a, 'b': b})
            return redirect(url_for('uniforme', **params))

        elif distribution == 'exponencial':
            media = float(request.form['media'])
            params.update({'media': media})
            return redirect(url_for('exponencial', **params))

        elif distribution == 'normal':
            media_normal = float(request.form['media_normal'])
            desviacion = float(request.form['desviacion'])
            params.update({'media_normal': media_normal, 'desviacion': desviacion})
            return redirect(url_for('normal', **params))

    return render_template('main_menu.html')

@app.route('/uniforme')
def uniforme():
    cantidad = int(request.args.get('cantidad', 0))
    visualizar = request.args.get('visualizar') == 'True'
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = generar_dist_uniforme(a, b, cantidad)
    hist, frequency, intervals = graficar_histograma(result, int(request.args.get('intervalos', 10)))
    archivo_histograma = guardar_imagen(hist, 'histogram_uniforme.png')
    tabla = tabla_frecuencias(intervals, frequency)
    print(tabla)
    return render_template('distribution.html', distr='uniforme', show_matrix=visualizar, items=result, histogram_url=archivo_histograma, tabla=tabla)

@app.route('/exponencial')
def exponencial():
    cantidad = int(request.args.get('cantidad', 0))
    visualizar = request.args.get('visualizar') == 'True'
    media = float(request.args.get('media', 0))
    result = generar_dist_exponencial(media, cantidad)
    hist, frequency, intervals = graficar_histograma(result, int(request.args.get('intervalos', 10)))
    archivo_histograma = guardar_imagen(hist, 'histogram_exponencial.png')
    
    return render_template('distribution.html', distr='exponencial', show_matrix=visualizar, items=result, histogram_url=archivo_histograma, tabla=tabla_frecuencias(intervals, frequency))

@app.route('/normal')
def normal():
    cantidad = int(request.args.get('cantidad', 0))
    visualizar = request.args.get('visualizar') == 'True'
    media_normal = float(request.args.get('media_normal', 0))
    desviacion = float(request.args.get('desviacion', 0))
    result = generar_dist_normal(media_normal, desviacion, cantidad)
    hist, frequency, intervals = graficar_histograma(result, int(request.args.get('intervalos', 10)))
    archivo_histograma = guardar_imagen(hist, 'histogram_normal.png')
    
    return render_template('distribution.html', distr='normal', show_matrix=visualizar, items=result, histogram_url=archivo_histograma, tabla=tabla_frecuencias(intervals, frequency))


if __name__ == "__main__":
    app.run()