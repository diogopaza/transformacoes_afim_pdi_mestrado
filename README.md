<h1>Rotacionando uma imagem</h1>
<p>Em latin affinis significa "conectado com" ou que possui conexão. Uma das transformações em geometria que também é 
utilizada em processamento digital de imagem se chama affine.</p>
<p>Rotação é um tipo de transformação affine</p>
<h3>Exemplo 1 rotação de imagem  </h3>

import cv2

imagem = cv2.imread("jogador.jpg")
altura, largura = imagem.shape[:2]
ponto_inicial = cv2.getRotationMatrix2D( (largura, altura), 45,0.5)

imagem_rotacionada = cv2.warpAffine( imagem, ponto_inicial, (largura,altura))
 
cv2.imshow("janela", imagem_rotacionada)

<h3>Exemplo 3 transformação afim</h3>

import cv2<br>
import numpy as np<br>

imagem = cv2.imread("grid.jpg")<br>
altura, largura = imagem.shape[:2]
cv2.circle( imagem, (83,90), 10, (0,0,255), -1) na sequencia os paramentros passados são a imagem onde o círculo será desenhado,
o local onde o círculo deve ficar na imagem, o terceiro parametro é o raio do círculo o quarto é a cor do círculo e por último caso o valor seja negativo indica que o círculo deve ser preenchido.
cv2.circle( imagem, (447,90), 10, (0,0,255), -1)
cv2.circle( imagem, (83,468), 10, (0,0,255), -1)

ponto1 = np.float32( [ [83,90],[447,90],[83,472]])
ponto1 = np.float32( [ [0,0],[447,90],[150,472]])

matriz = cv2.getAffineTransform( ponto1, ponto2)
imagem_transformacao_afim= cv2.warpAffine( imagem, matriz, (largura, altura))

cv2.imshow("Input", imagem)<br>
cv2.imshow("Output", imagem_transforamcao_afim)<br>
cv2.waitKey(0)<br>
cv2.destroyAllWindows()<br>




<h2>Translação(deslocamento)</h2>
<p></p>


<h1>Resolvendo problema de Rotação do OpenCV</h1>
<h4>Tadução do artigo https://www.pyimagesearch.com/2017/01/02/rotate-images-correctly-with-opencv-and-python/</h4>
<h4>Implementando uma função de rotação que não corta suas imagens</h4>
<p>Vamos começar dizendo que não há nada de errado com cv2.getRotationMatrix2D e cv2.warpAffine funções que são usadas
para rotacionar imagens no OpenCV.</p>
<p>Na verdade, essas funções nos dão mais liberdade nós nos sentimos mais confortáveis com elas.( mais ou menos
como gerenciar memoria em C versos coletor de lixo do Java. )</p>
<p>A função cv2.getRotation2D não se importa se nós gostariamos que toda a imagem girada fosse mantida.  </p>

<p>Não importa se as imagens são cortadas.</p>
<p>Isso não vai ajudar você, vai ser um tiro no pé( eu descobri isso da maneira mais difícil, eu levei
3 semanas para resolver o problema. ) </p>
<p>Em vez disso, oque você precisa é entender oque é a matriz de rotação e como ela é construída.</p>
<p>Você ve quando gira ima imagem com OpenCV você chama cv2.getRotationMatrix2D que retorna uma matriz M que se parece com isso:</p>
<p>Esta matriz parece assustadora, mas eu prometo a você: não é</p>
<p>Para entender isso, vamos assumir que queremos girar nossa imagem 0 graus sobre o centro ( cx, cy )coor
denadas em alguma escala( menor ou maior)</p>
<p>Podemos então inserir valores para gama e beta</p>
beta = scale * cos0 e beta=scale*sin0
<p>Tudo pronto para a rotação simples - mas não leva em conta oque acontece se uma imagem é cortada ao longo das bordas. Como podemos resolver isso?</p>
<p>A reposta está na função rotate_bound</p>



<p>Na linha 41 nos definimos nossa função rotate_bound</p>
<p>Esse metódo aceita uma imagem como entrada e um angulo pra rotaciona-la</p>
<p>Assumimos que vamos girar nossa imagem sobre esse centro( x,y )-coordenadas, então nós
determinamos esses valores nas linhas....</p>
<p>Dadas essas coordenadas podemos chamar cv2.getRotationMatrix2D para obter nossa matriz de rotação M( linha...).</p>
<p>Porém para ajustar para qualquer imagem precisamos fazer alguns ajustes</p>
<p>Começamos pegando os valores de seno e cossenos da nossa matriz de rotação M( linhas... )</p>
<p>Isso nos permite calcular a nova largura e altura da imagem girada, garantindo que nenhuma parte da imagem seja cortada</p>
<p>Uma vez que sabemos a nova largura e altura, podemos modificar nossa matriz de rotação mais uma vez( linhas...) </p>
<p>Finalmente cv2.warpAffine é chamada na última linha para rotacionar a imagem atual usando OpenCV 
garantindo que nenhuma imagem seja cortada</p>







