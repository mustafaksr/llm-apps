    const container = document.getElementById('flashcardContainer');
    const mInput = document.getElementById('mInput');
    const nInput = document.getElementById('nInput');

    function createFlashcards(frontTextArray, backTextArray) {
      const m = parseInt(mInput.value);
      const n = parseInt(nInput.value);
      // Calculate grid dimensions based on m and n
      const numRows = m;
      const numCols = n;
      // Calculate the total number of flashcards
      const numCards = numRows * numCols;
      // Clear the container before creating new flashcards
      container.innerHTML = '';
      // Create and append flashcards to the container
      for (let i = 0; i < numCards; i++) {
        const flashcard = document.createElement('div');
        flashcard.classList.add('flashcard');
        const flipper = document.createElement('div');
        flipper.classList.add('flipper');

        const front = document.createElement('div');
        front.classList.add('front');
        front.textContent = frontTextArray[i];
        const back = document.createElement('div');
        back.classList.add('back');
        back.textContent = backTextArray[i];

        flipper.appendChild(front);
        flipper.appendChild(back);
        flashcard.appendChild(flipper);
        flashcard.addEventListener('click', () => {
          flashcard.classList.toggle('flipped');
        });
        container.appendChild(flashcard);
      }

      // Set CSS variables based on grid dimensions
      document.documentElement.style.setProperty('--grid-rows', numRows);
      document.documentElement.style.setProperty('--grid-cols', numCols);
      document.documentElement.style.setProperty(
        '--max-width',
        `calc(${numCols} * var(--flashcard-width) + (${numCols} + 1) * 10px)`
      );
      document.documentElement.style.setProperty(
        '--max-height',
        `calc(${numRows} * var(--flashcard-height) + (${numRows} + 1) * 10px)`
      );
    }

    // Create initial flashcards on page load
    createFlashcards([], []);

    // Re-create flashcards on form submission
    document.getElementById('gridForm').addEventListener('submit', (event) => {
      event.preventDefault();
      const query = document.getElementById('queryInput').value;
      const formData = new FormData(event.target);
      const m = parseInt(formData.get('mInput'));
      const n = parseInt(formData.get('nInput'));
      const url = '/flashcards';
      fetch(url, {
        method: 'POST',
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          createFlashcards(data.front, data.back);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    });