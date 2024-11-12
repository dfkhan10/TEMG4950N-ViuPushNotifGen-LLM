import React, { useEffect, useState } from "react";
import ToggleSwitch from './ToggleSwitch';
import Header from './Header';
import Slider from './Slider';
import TrendComponent from "./TrendComponent";
import { useNavigate } from 'react-router-dom';

const ViuDataContext = React.createContext({
  viuData: [], fetchViudata: () => {}
})

export const Homepage = () => {
  //Call a get api to retrieve viu data for dropdown menus of cast and show
  const [viuDatas, setViuDatas] = useState([])

  const fetchViuData = async () => {
    const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/viuData`);
    const data = await response.json()
    console.log(data)
    setViuDatas(data.key)
  }

  useEffect(() => { fetchViuData() }, [])

  // State to track the active button
  const [activeButton, setActiveButton] = useState('generator'); // State for the Active page
  const [promotionType, setPromotionType] = useState(''); // State for the Promotion type
  const [creativity, setCreativity] = useState(0); // State for the creativity slider
  const [age, setAge] = useState(''); // State for age
  const [isFormEnabled, setIsFormEnabled] = useState(false);
  const [showTrends, setShowTrends] = useState(false);

  const navigate = useNavigate();

  const handleGenerate = () => {
    navigate('/generation'); 
  };


  const isFormValid = () => {
    return promotionType &&
           age && 
           document.querySelector('input[placeholder="Enter Content Name"]').value &&
           (promotionType === 'cast-driven' ? document.querySelector('input[placeholder="Enter Star Name"]').value : true);
  };

  useEffect(() => {
    setIsFormEnabled(isFormValid());
  }, [promotionType, age]); 

  const handlePromotionTypeChange = (event) => {
    setPromotionType(event.target.value);
  };

  const handleGenerateTrends = () => {
    setShowTrends(true);
    // Include any logic to generate trends here
  };

  // Function to handle button clicks
  const handleButtonClick = (button) => {
    setActiveButton(button);
  };

  return (
    <div className="h-screen flex flex-col">
    <Header activeButton={activeButton} handleButtonClick={handleButtonClick} />
    
    {/* Main Content Area */}
    <div className="flex flex-grow bg-[#F5F5F5]">
        {/* First Section (3/5) */}
        <div className="flex-grow flex flex-col items-center">
          <div className="flex items-center pr-11 mb-8 mt-6">
            <img src="viu_logo.png" className="w-60 ml-8" alt="VIU Logo" />
            <h2 className="text-5xl font-bold text-[#F5B919] ml-8">Push Notification Generator</h2>
          </div>

          {/* Input Fields Section */}
          <div className="flex flex-col w-full px-36">
            <div className="flex space-x-10 justify-center">
              
            {/* Promotion Type Dropdown */}
            <div className="flex-grow mb-4 w-full">
              <div className="flex">
                <label className="block text-sm font-bold text-lg text-gray-700">Promotion Type</label>
                <label className="text-red-400 font-bold text-lg ml-1">*</label>
              </div>
              <select
                className="mt-1 block h-8 w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919]"
                value={promotionType}
                onChange={handlePromotionTypeChange}
              >
                <option value="" disabled hidden>
                  Select Promotion
                </option>
                <option value="content-based">Content-based promotion</option>
                <option value="cast-driven">Cast-driven promotion</option>
              </select>
            </div>

            <div className="w-full">
              <Slider value={creativity} onChange={(e) => setCreativity(e.target.value)} />
            </div>
            
          </div>

          <div className="grid grid-cols-2 gap-4">
              {/* Content Name */}
              <div className="mb-4">
                <div className="flex">
                  <label className="block text-sm font-bold text-lg text-gray-700">Content Name</label>
                  <label className="text-red-400 font-bold text-lg ml-1">*</label>
                </div>
                <input
                  type="text" // Corrected from "dropdown" to "text"
                  placeholder="Enter Content Name"
                  className="mt-1 block w-full h-8 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919]"
                  disabled={!promotionType}
                />
              </div>

              {/* Star Name */}
              <div className="mb-4">
                <div className="flex">
                  <label className="block text-sm font-bold text-lg text-gray-700">Star Name</label>
                  <label className="text-red-400 font-bold text-lg ml-1">*</label>
                </div>
                <input
                  type="text"
                  placeholder="Enter Star Name"
                  className="mt-1 block w-full h-8 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919]"
                  disabled={!promotionType || promotionType === 'content-based'} // Disable if no promotion type is selected or if content-based is selected
                />
              </div>

              {/* Age Dropdown */}
              <div className="mb-4">
                <div className="flex">
                  <label className="block text-sm font-bold text-lg text-gray-700">Target Age</label>
                  <label className="text-red-400 font-bold text-lg ml-1">*</label>
                </div>
                <select
                  className="mt-1 block h-8 w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919]"
                  value={age}
                  onChange={(e) => setAge(e.target.value)} // Corrected to e.target.value
                >
                  <option value="" disabled hidden>Select Age</option>
                  <option value="Bahasa Inggeris">18-29</option>
                  <option value="Bahasa Melayu">30-49</option>
                  <option value="Bahasa Melayu">50-64</option>
                  <option value="Bahasa Melayu">65 and above</option>
                </select>
              </div>

              <div className="flex flex-col">
                  <ToggleSwitch label="Include Local Lingo?" />
                  <ToggleSwitch label="Include Emojis?" />
              </div>
            </div>

            {/* Additional Input Field */}
            <div className="flex flex-col w-full mb-4">
                <label className="block text-sm font-bold text-lg text-gray-700 mb-2">Additional Input</label>
                <textarea
                  placeholder="Enter additional information here..."
                  className="mt-1 block w-full h-60 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919] p-2"
                />
              </div>

              {/* Generate Button */}
              <div className="flex justify-center mb-4">
                <button className={`bg-[#F5B919] w-full text-3xl text-black font-bold py-3 px-6 rounded-lg shadow-md hover:bg-yellow-600 transition duration-300 ${isFormEnabled ? '' : 'cursor-not-allowed opacity-50'}`} disabled={!isFormEnabled} onClick={handleGenerate} >
                  Generate
                </button>
              </div>
          </div>
        </div>

        {/* Vertical Line Separator */}
        <div className="w-1 bg-gray-300 my-10"></div>

        {/* Second Section (2/5) */}
        <div className="flex flex-col justify-center items-center w-2/5">
          <div className="flex items-start">
            <h2 className="text-2xl font-bold">Trends</h2>
          </div>
          <div className="w-4/5 h-5/6 bg-white flex justify-center items-center rounded-lg shadow-md mt-4">
            {!showTrends ? (
              <button className={`bg-[#F5B919] text-black font-bold py-2 px-4 hover:bg-yellow-600 rounded-full cursor-not-allowed" ${isFormEnabled ? '' : 'cursor-not-allowed opacity-50'}`} disabled={!isFormEnabled} onClick={handleGenerateTrends} >
                Generate Trends
              </button>
            ) : (
              <div className="flex flex-col w-full">
                <TrendComponent title="Celebrity Spotlight" description="Kim Na Huels' latest comments at the K-Drama press conference"/>
                <TrendComponent title="Tropical Trends" description="Residents told to stay home as temperatures set to cross 35 degrees this week"/>
                <TrendComponent title="Holiday Spirit" description="Public holiday this Saturday on Malaysia Day"/>
                <TrendComponent title="Pop Culture" description="K-pop group Black Pink is coming to Malaysia for their world tour"/>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

