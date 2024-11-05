import TextBox from "../components/TextBox";
import React, { useEffect, useState } from "react";

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
  const [activeButton, setActiveButton] = useState('');
  const [promotionType, setPromotionType] = useState(''); // State for promotion type
  const [age, setAge] = useState(''); // State for age
  const [language, setLanguage] = useState(''); // State for language
  const [includeLingo, setIncludeLingo] = useState(false); // State for local lingo toggle
  const [includeEmojis, setIncludeEmojis] = useState(false); // State for emojis toggle

  const handlePromotionTypeChange = (event) => {
    setPromotionType(event.target.value);
  };

  // Function to handle button clicks
  const handleButtonClick = (button) => {
    setActiveButton(button);
  };

  return (
    <div className="h-screen flex flex-col">
    {/* White Box at the Top */}
    <div className="bg-white h-1/6 flex flex-col justify-between p-4 shadow-md">
      <div className="flex flex-col justify-between ml-3">
        <h1 className="text-xl font-bold mt-3">Copywriter AI</h1>
        <p className="text-gray-500 mt-3">
          With our Copywriter AI, you can generate multilingual text off a prompt, a show or an actor.
        </p>
      </div>
      <div className="flex pl-3">
          <button
            className={`text-pink-500 py-2 px-4 font-bold ${activeButton === 'generator' ? 'border-b-4 border-pink-500' : ''}`}
            onClick={() => handleButtonClick('generator')}
          >
            AI Generator
          </button>
          <button
            className={`text-pink-500 py-2 px-4 font-bold ${activeButton === 'audit' ? 'border-b-4 border-pink-500' : ''}`}
            onClick={() => handleButtonClick('audit')}
          >
            Audit
          </button>
        </div>
    </div>

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
            <div className="flex-grow mb-4">
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

              {/* Creativity Slider */}
              <div className="flex-grow mb-4">
                <div className="flex">
                  <label className="block text-lg font-bold text-gray-700">Creativity</label>
                  <label className="text-red-400 font-bold text-lg ml-1">*</label>
                </div>
                <input
                  type="range"
                  min="0"
                  max="100"
                  className="mt-4 w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                  style={{
                    accentColor: '#3B82F6', 
                  }}
                />
                <style jsx>{`
                  input[type='range'] {
                    -webkit-appearance: none;
                    width: 100%;
                  }
              
                  input[type='range']::-webkit-slider-thumb {
                    -webkit-appearance: none;
                    appearance: none;
                    width: 24px; /* Increase the size of the thumb */
                    height: 24px; /* Increase the size of the thumb */
                    border-radius: 50%;
                    background: #3B82F6; /* Tailwind blue-500 color */
                    cursor: pointer;
                    margin-top: -1px; /* Center the thumb vertically */
                  }
              
                  input[type='range']::-webkit-slider-runnable-track {
                    height: 22px; /* Height of the track */
                    background: #e5e7eb; /* Color of the unfilled portion */
                    border-radius: 5px;
                  }
                `}</style>
              </div>
            </div>

            <div className="flex space-x-10 justify-center">
              {/* Content Name */}
              <div className="flex-grow mb-4">
                <div className="flex">
                  <label className="block text-sm font-bold text-lg text-gray-700">Content Name</label>
                  <label className="text-red-400 font-bold text-lg ml-1">*</label>
                </div>
                <input
                  type="dropdown"
                  placeholder="Enter Content Name"
                  className="mt-1 block w-full h-8 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919]"
                  disabled={!promotionType}
                />
              </div>
              
              {/* Star Name*/}
              <div className="flex-grow mb-4">
                <div className="flex">
                  <label className="block text-sm font-bold text-lg text-gray-700">Star Name</label>
                  <label className="text-red-400 font-bold text-lg ml-1">*</label>
                </div>
                <input
                  type="text"
                  placeholder="Enter Star Name"
                  className="mt-1 block w-full h-8 border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919]"
                  disabled={!promotionType} 
                />
              </div>
            </div>

            <div className="flex">
              {/* Age Dropdown */}
              <div className="flex-grow mb-4 mr-8">
                <div className="flex">
                  <label className="block text-sm font-bold text-lg text-gray-700">Age</label>
                  <label className="text-red-400 font-bold text-lg ml-1">*</label>
                </div>
                <select
                  className="mt-1 block h-8 w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919]"
                  value={age}
                  onChange={(e) => setAge(e.target.age)}
                >
                  <option value="" disabled hidden>Select Age</option>
                  <option value="Bahasa Inggeris">18-29</option>
                  <option value="Bahasa Melayu">30-49</option>
                  <option value="Bahasa Melayu">50-64</option>
                  <option value="Bahasa Melayu">65 and above</option>
                </select>
              </div>

              {/* Language Dropdown */}
              <div className="flex-grow mb-4 mr-8">
                <div className="flex">
                  <label className="block text-sm font-bold text-lg text-gray-700">Language</label>
                  <label className="text-red-400 font-bold text-lg ml-1">*</label>
                </div>
                <select
                  className="mt-1 block h-8 w-full border border-gray-300 rounded-md shadow-sm focus:ring focus:ring-[#F5B919] focus:border-[#F5B919]"
                  value={language}
                  onChange={(e) => setLanguage(e.target.value)}
                >
                  <option value="" disabled hidden>Select Language</option>
                  <option value="Bahasa Inggeris">Bahasa Inggeris</option>
                  <option value="Bahasa Melayu">Bahasa Melayu</option>
                </select>
              </div>
              
              <div className="flex flex-col">
                {/* Toggle for Include Local Lingo */}
                <div className="flex items-center mb-4">
                  <label htmlFor="includeLingo" className="text-lg mr-2">Include Local Lingo?</label>
                  <div className="relative">
                    <input
                      type="checkbox"
                      id="includeLingo"
                      checked={includeLingo}
                      onChange={() => setIncludeLingo(!includeLingo)}
                      className="hidden" // Hide the default checkbox
                    />
                    <div 
                      className={`w-12 h-6 flex items-center bg-gray-300 rounded-full p-1 cursor-pointer transition-colors duration-300 ${includeLingo ? 'bg-blue-500' : ''}`} 
                      onClick={() => setIncludeLingo(!includeLingo)}
                    >
                      <div className={`w-4 h-4 bg-white rounded-full shadow-md transform transition-transform duration-300 ${includeLingo ? 'translate-x-6' : 'translate-x-0'}`} />
                    </div>
                  </div>
                </div>

                {/* Toggle for Include Local Lingo */}
                <div className="flex items-center mb-4">
                  <label htmlFor="includeEmojis" className="text-lg mr-11">Include Emojis?</label>
                  <div className="relative">
                    <input
                      type="checkbox"
                      id="includeLingo"
                      checked={includeEmojis}
                      onChange={() => setIncludeEmojis(!includeEmojis)}
                      className="hidden" // Hide the default checkbox
                    />
                    <div 
                      className={`w-12 h-6 flex items-center bg-gray-300 rounded-full p-1 cursor-pointer transition-colors duration-300 ${includeEmojis ? 'bg-blue-500' : ''}`} 
                      onClick={() => setIncludeEmojis(!includeEmojis)}
                    >
                      <div className={`w-4 h-4 bg-white rounded-full shadow-md transform transition-transform duration-300 ${includeEmojis ? 'translate-x-6' : 'translate-x-0'}`} />
                    </div>
                  </div>
                </div>
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
                <button className="bg-[#F5B919] w-full text-3xl text-black font-bold py-3 px-6 rounded-lg shadow-md hover:bg-yellow-600 transition duration-300">
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
            <button className="bg-gray-300 text-gray-500 py-2 px-4 rounded-full cursor-not-allowed" disabled>
              Generate Trends
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
