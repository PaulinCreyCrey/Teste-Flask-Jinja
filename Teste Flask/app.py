from flask import Flask, render_template
from Classes import Restaurante, Comentario

app = Flask(__name__)

comentario1_sabor = Comentario('edv_niam2022', 'Cheguei 13:30 para almoçar com a minha família e quase não tinha comida. Só um resto, não tinha prato limpo, churrasco teria que esperar e tudo muito sujo. Muito ruim.')
comentario2_sabor = Comentario('marciaguedes21', 'Cheguei com um grupo de 6 pessoas. Não queríamos almoçar, então só tomamos cerveja bem gelada e comemos pasteis saborosos! O atendimento foi nota 10! O garçon foi bem atencioso com a gente!')
comentario3_sabor = Comentario('reteixeira1', 'Comemos uma deliciosa pizza de provolone e além do sabor, nos recordaremos do excelente atendimento que recebemos no restaurante. Pessoas simples e super acolhedoras. Recomendo!')
Comentario_sabor = [comentario1_sabor, comentario2_sabor, comentario3_sabor]

comentario1_sputnik = Comentario('236cristinav', 'O restaurante serve comida a quio com churrasco e comida japonesa. A comida é bem preparada e o atendimento foi muito bom. O local tem área para crianças brincarem e serve uma pequena sobremesa e água saborizada grátis.')
comentario2_sputnik = Comentario('michellessccastro', 'Bastante variedade (saladas, churrasco, comida japonesa..), bom atendimento....certamente voltarei qd estiver na região de Vassouras.')
comentario3_sputnik = Comentario('Teatro2022', 'Não tinha galinha com quiabo!!!! Lamentável! É o melhor prato de fogão a lenha! Os demais pratos são muito bons! Comida bem feita por preço justo!')
Comentario_sputnik = [comentario1_sputnik, comentario2_sputnik, comentario3_sputnik]

sabor_do_vale = Restaurante(0, 'Sabor do Vale', 'sabordovale.jpg', 'Av. Exp.Osvaldo de Almeida Ramos, 86', Comentario_sabor )
sputnik = Restaurante(1, 'sputnik', 'sputnik.jpg', 'Travessa Americo Brasileiro 50 Pedro Ii', Comentario_sputnik)
restaurante_lista = [sabor_do_vale, sputnik]

@app.route('/')
def inicio():
 return render_template('tela_inicial.html', restaurantes=restaurante_lista)

@app.route('/restaurante/<id>')
def restaurante(id):
 return render_template('restaurante.html',  restaurante=restaurante_lista[int(id)])







