<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>
<body>

    <main> 
        <div class="fundo"> <!-Cria uma div com nome de "fundo", que seria o fundo da página->
            <div class="calculadora"> <!-Cria uma outra div da div "fundo" com o nome de "calculadora"->
                <h1>Calculadora</h1> 
                <p id="resultado"></p>
                <table>
                    <tr>
                        <td><button class="botao" onclick="clean()">C</button></td> <!-A tag table é usada para tabela, sem as tags "tr" e "td" não resultam em nada–>
                        <td><button class="botao" onclick="back()"><</button></td> 
                        <td><button class="botao" onclick="insert('/')">/</button></td>
                        <td><button class="botao" onclick="insert('*')">x</button></td>
                    </tr>
                    <tr>
                        <td><button class="botao" onclick="insert('7')">7</button></td>
                        <td><button class="botao" onclick="insert('8')">8</button></td>
                        <td><button class="botao" onclick="insert('9')">9</button></td>
                        <td><button class="botao" onclick="insert('-')">-</button></td>
                    </tr>
                    <tr>
                        <td><button class="botao" onclick="insert('4')">4</button></td>
                        <td><button class="botao" onclick="insert('5')">5</button></td>
                        <td><button class="botao" onclick="insert('6')">6</button></td>
                        <td><button class="botao" onclick="insert('+')">+</button></td>
                    </tr>
                    <tr>
                        <td><button class="botao" onclick="insert('1')">1</button></td>
                        <td><button class="botao" onclick="insert('2')">2</button></td>
                        <td><button class="botao" onclick="insert('3')">3</button></td>
                        <td rowspan=2><button class="botao" style="height: 122px" onclick="calcular()">=</button></td> <!- rowspan para expandir 2 linhas->
                    </tr>
                    <tr>
                        <td colspan=2><button class="botao" style="width:122px" onclick="insert('0')">0</button></td> <!- colspan para expandir 2 colunas->
                        <td><button class="botao" onclick="insert('.')">.</button></td> 
                    </tr>
                </table>
            </div>
        </div>
    </main>

    <footer> 

    </footer>   

</body>
</html>