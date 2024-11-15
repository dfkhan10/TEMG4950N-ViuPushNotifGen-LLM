// SelectThumbnail.jsx
import React, { useState, useEffect } from 'react';

const SelectThumbnail = ({ onClose }) => {
    const [currentIndex, setCurrentIndex] = useState(0);
    const [logoPosition, setLogoPosition] = useState({ x: 50, y: 50 }); // Starting position for the logo
    const [buttonPosition, setButtonPosition] = useState({ x: 100, y: 100 }); // Starting position for the button
    const [draggingLogo, setDraggingLogo] = useState(false);
    const [draggingButton, setDraggingButton] = useState(false);
    const thumbnails = [
        "thumbnail1.png", // Replace with your image sources
        "thumbnail2.png",
        "thumbnail1.png",
        "thumbnail2.png"
    ];

    const handleNext = () => {
        setCurrentIndex((prevIndex) => (prevIndex + 1) % thumbnails.length);
    };

    const handlePrevious = () => {
        setCurrentIndex((prevIndex) => (prevIndex - 1 + thumbnails.length) % thumbnails.length);
    };

    const handleMouseDown = (e, setDragging) => {
        e.preventDefault();
        setDragging(true);
    };

    const handleMouseMove = (e) => {
        if (draggingLogo || draggingButton) {
            const image = document.querySelector('.thumbnail-image');
            const rect = image.getBoundingClientRect(); // Get the image's bounding rectangle
            const offsetX = e.clientX - rect.left; // Mouse position relative to the left of the image
            const offsetY = e.clientY - rect.top;  // Mouse position relative to the top of the image
    
            if (draggingLogo) {
                const logoWidth = 248.2-115.625; // Replace with actual logo width
                const logoHeight = 96; // Replace with actual logo height
                const newX = Math.max(115.625+0, Math.min(offsetX - logoWidth / 2, rect.width - logoWidth));
                const newY = Math.max(0, Math.min(offsetY - logoHeight / 2, rect.height - logoHeight));
                setLogoPosition({ x: newX, y: newY });
            } else if (draggingButton) {
                const buttonWidth = 190-115.625; // Replace with actual button width
                const buttonHeight = 48; // Replace with actual button height
                const newX = Math.max(115.625+0, Math.min(offsetX - buttonWidth / 2, rect.width - buttonWidth));
                const newY = Math.max(0, Math.min(offsetY - buttonHeight / 2, rect.height - buttonHeight));
                setButtonPosition({ x: newX, y: newY });
            }
        }
    };

    const handleMouseUp = () => {
        setDraggingLogo(false);
        setDraggingButton(false);
    };

    useEffect(() => {
        // Attach mousemove and mouseup listeners to the document
        document.addEventListener('mousemove', handleMouseMove);
        document.addEventListener('mouseup', handleMouseUp);

        // Clean up the event listeners on component unmount
        return () => {
            document.removeEventListener('mousemove', handleMouseMove);
            document.removeEventListener('mouseup', handleMouseUp);
        };
    }, [draggingLogo, draggingButton]);

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
            <div className="bg-white p-6 rounded-lg shadow-lg w-1/2 relative">
                <h2 className="text-2xl font-bold mb-2 absolute top-4 left-4 pl-2">Select Thumbnail</h2>
                <button 
                    className="absolute top-4 right-4 text-gray-600 text-4xl pr-2"
                    onClick={onClose}
                >
                    &times; {/* Cross icon */}
                </button>
                <p className="mb-4 pt-6">Choose a thumbnail from the show or episode that will be featured in the push notification.</p>
                <div className="flex flex-col items-center relative">
                    <img 
                        src={thumbnails[currentIndex]} 
                        alt="Thumbnail" 
                        className="w-3/4 h-auto mb-2 thumbnail-image" 
                    />
                    {/* Draggable Logo */}
                    <img 
                        src="viu_logo.png" 
                        alt="Viu Logo" 
                        className="absolute cursor-move h-24" 
                        style={{ left: `${logoPosition.x}px`, top: `${logoPosition.y}px` }} 
                        onMouseDown={(e) => handleMouseDown(e, setDraggingLogo)}
                    />
                    {/* Draggable Call to Action Button */}
                    <button
                        className="absolute border-2 border-[#F5B919] bg-white text-[#F5B919] text-lg py-2 px-4 rounded cursor-move rounded-full"
                        style={{ left: `${buttonPosition.x}px`, top: `${buttonPosition.y}px` }}
                        onMouseDown={(e) => handleMouseDown(e, setDraggingButton)}
                    >
                        Tonton Sekarang &gt;
                    </button>
                    <div className="flex items-center mt-2">
                        <button onClick={handlePrevious} className="text-xl text-gray-600 mr-2">&lt;</button>
                        <span className='text-xl'>{currentIndex + 1} / {thumbnails.length}</span>
                        <button onClick={handleNext} className="text-xl text-gray-600 ml-2">&gt;</button>
                    </div>
                </div>
                <div className="flex justify-end">
                    <button 
                        className="bg-white text-[#3078BE] border-2 border-[#3078BE] py-3 px-6 rounded mr-2 hover:bg-[#3078BE] hover:text-white transition duration-300"
                        onClick={onClose}
                    >
                        Cancel
                    </button>
                    <button 
                        className="bg-white text-[#3078BE] border-2 border-[#3078BE] py-3 px-6 rounded hover:bg-[#3078BE] hover:text-white transition duration-300"
                    >
                        Next
                    </button>
                </div>
            </div>
        </div>
    );
};

export default SelectThumbnail;