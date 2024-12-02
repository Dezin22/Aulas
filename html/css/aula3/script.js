// Variáveis para controlar o jogador atual e o estado do jogo
let currentPlayer = 'o'; // 'o' para bola, 'x' para X
let gameOver = false; // Controla se o jogo terminou

// Pegando todas as células da grid
const cells = document.querySelectorAll('.cell');
const messageDiv = document.getElementById('message');
const resetBtn = document.getElementById('resetBtn');
const reiniciar = document.getElementById('reiniciar')

// Função para verificar se alguém ganhou
function checkWinner() {
  const winPatterns = [
    [0, 1, 2], // Linha superior
    [3, 4, 5], // Linha do meio
    [6, 7, 8], // Linha inferior
    [0, 3, 6], // Coluna esquerda
    [1, 4, 7], // Coluna do meio
    [2, 5, 8], // Coluna direita
    [0, 4, 8], // Diagonal principal
    [2, 4, 6]  // Diagonal secundária
  ];

  // Checar se algum padrão vencedor foi alcançado
  for (let pattern of winPatterns) {
    const [a, b, c] = pattern;
    if (cells[a].classList.contains(currentPlayer) &&
        cells[b].classList.contains(currentPlayer) &&
        cells[c].classList.contains(currentPlayer)) {
      return true;
    }
  }
  return false;
}

// Função que lida com o clique nas células
function handleClick(event) {
  const cell = event.target;
  
  // Se a célula já foi marcada ou o jogo acabou, nada acontece
  if (cell.classList.contains('x') || cell.classList.contains('o') || gameOver) {
    return;
  }
  
  // Marca a célula com o símbolo do jogador atual
  cell.classList.add(currentPlayer);

  // Verifica se o jogador atual venceu
  if (checkWinner()) {
    gameOver = true;
    messageDiv.textContent = `Parabéns, jogador ${currentPlayer === 'o' ? 'bola' : 'X'}! Você venceu!`;
    resetBtn.style.display = 'block';
    reiniciar.style.display = 'block';
    return;
  }

  // Alterna o jogador
  currentPlayer = currentPlayer === 'o' ? 'x' : 'o';
}

// Função para reiniciar o jogo
function resetGame() {
  // Limpa todas as células
  cells.forEach(cell => cell.classList.remove('o', 'x'));

  // Reseta as variáveis de controle
  currentPlayer = 'o';
  gameOver = false;
  messageDiv.textContent = '';
  resetBtn.style.display = 'none';
  reiniciar.style.display = 'block';
}

// Adiciona o evento de clique a todas as células
cells.forEach(cell => {
  cell.addEventListener('click', handleClick);
});

// Adiciona o evento de reinício do jogo
resetBtn.addEventListener('click', resetGame);
reiniciar.addEventListener('click',resetGame);