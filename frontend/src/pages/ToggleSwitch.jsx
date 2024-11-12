// ToggleSwitch.js
import React, { useState } from 'react';

const ToggleSwitch = ({ label }) => {
  // State for the toggle
  const [includeLingo, setIncludeLingo] = useState(false);

  return (
    <div className="flex justify-between items-center mb-4"> {/* Use justify-between for alignment */}
      <label htmlFor="includeLingo" className="text-lg">{label}</label> {/* Use the label prop */}
      <div className="relative">
        {/* Hidden Checkbox */}
        <input
          type="checkbox"
          id="includeLingo"
          checked={includeLingo}
          onChange={() => setIncludeLingo(!includeLingo)}
          className="hidden" // Hide the default checkbox
        />
        {/* Custom Toggle Switch */}
        <div 
          className={`w-12 h-6 flex items-center rounded-full p-1 cursor-pointer transition-colors duration-300 ${includeLingo ? 'bg-blue-500' : 'bg-gray-300'}`} 
          onClick={() => setIncludeLingo(!includeLingo)}
        >
          {/* Circle that moves */}
          <div className={`w-4 h-4 bg-white rounded-full shadow-md transform transition-transform duration-300 ${includeLingo ? 'translate-x-6' : 'translate-x-0'}`} />
        </div>
      </div>
    </div>
  );
};

export default ToggleSwitch;