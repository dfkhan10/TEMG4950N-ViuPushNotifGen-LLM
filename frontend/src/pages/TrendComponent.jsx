import React, { useState } from 'react';
// hi
const TrendComponent = ({ title, imageSrc }) => {
    const [checked, setChecked] = useState(false);

    const handleCheckboxChange = () => {
        setChecked(!checked);
    };

    return (
        <div className='px-4 sm:px-2 py-3'>
            <div className={`flex items-center rounded-lg p-4 mb-4 shadow-md ${checked ? 'bg-yellow-300 border-black' : 'bg-[#F5B919]'}`}>
                <div 
                    className={`w-4 h-4 border-2 rounded-lg flex items-center justify-center mr-4 cursor-pointer ${checked ? 'bg-gray-800' : 'bg-white'}`} 
                    onClick={handleCheckboxChange}
                >
                    {checked && <div className="w-2 h-2 bg-white rounded-full" />} {/* Show a small dot when checked */}
                </div>
                <div className='flex-1'>
                    <h3 className="text-md">{title}</h3>
                </div>
            </div>
        </div>
    );
};

export default TrendComponent;