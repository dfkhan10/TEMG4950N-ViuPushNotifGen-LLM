import React, { useState } from 'react';

const TextBox = ({ label }) => {
  const [value, setValue] = useState('');

  const handleChange = (e) => {
    setValue(e.target.value);
  };

  return (
    <div>
      <label>{label}</label>
      <input
        type="text"
        value={value}
        onChange={handleChange}
      />
    </div>
  );
};

export default TextBox;