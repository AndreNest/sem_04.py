from  user_interface import temparature_view
from  user_interface import pressure_view
from  user_interface import wind_speed_view

def create(devise = 1):
    style = 'style ="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, temparature_view(devise))
    html += '    <p {}>Wind_Speed: {} m/s</p>\n' \
        .format(style, wind_speed_view(devise))
    html += '    <p {}>Pressure: {} mmHg</p>\n' \
        .format(style, pressure_view(devise))
    html += '   </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html
