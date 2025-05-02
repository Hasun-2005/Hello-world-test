import React, { useState } from 'react';
import './Chessboard.css';

const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

const Chessboard: React.FC = () => {
  const [selected, setSelected] = useState<{ row: number; col: number } | null>(null);

  const handleClick = (row: number, col: number) => {
    setSelected({ row, col });

    const file = files[col];
    const rank = 8 - row;
    const coord = `${file}${rank}`;
    console.log(`Clicked square: ${coord}`);
  };

  const board = [];

  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
      const isDark = (row + col) % 2 === 1;
      const file = files[col];
      const rank = 8 - row;
      const coord = `${file}${rank}`;

      const isSelected = selected?.row === row && selected?.col === col;

      board.push(
        <div
          key={`${row}-${col}`}
          className={`tile ${isDark ? 'dark' : 'light'} ${isSelected ? 'selected' : ''}`}
          onClick={() => handleClick(row, col)}
        >
          <span className="coord">{coord}</span>
        </div>
      );
    }
  }

  return <div className="chessboard">{board}</div>;
};

export default Chessboard;

