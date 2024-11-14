import React, { useEffect, useState } from 'react';

// SpinnerOverlay component (for loading state)
const SpinnerOverlay = () => (
  <div className="spinner-overlay">
    <div className="spinner">Loading...</div>
  </div>
);

// Main ViuDataComponent
const ViuDataComponent = () => {
  const [viuDatas, setViuDatas] = useState([]); // State for storing fetched Viu data
  const [isLoading, setIsLoading] = useState(true); // State for loading status
  const [error, setError] = useState(null); // State for error handling

  // Fetch function to retrieve Viu data
  const fetchViuData = async () => {
    try {
      const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/viuData`);

      // Check if the response is OK (status code 200)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log(data); // Log the fetched data for debugging

      // Assuming data is an array of objects and you want to set it directly
      setViuDatas(data); // Update this line to set the data directly
    } catch (error) {
      setError(error.message); // Set error message if fetch fails
    } finally {
      setIsLoading(false); // Set loading to false after fetch is complete
    }
  };

  useEffect(() => {
    fetchViuData(); // Call the fetch function on component mount
  }, []); // Empty dependency array means this runs once on component mount

  // Render loading spinner while data is being fetched
  if (isLoading) {
    return <SpinnerOverlay />;
  }

  // Render error message if there was an error fetching data
  if (error) {
    return <div style={{ color: 'red' }}>Error: {error}</div>;
  }

  // Render the fetched data
  return (
    <div>
      {viuDatas.length > 0 ? (
        viuDatas.map((item, index) => (
          <div key={index}>
            <h3>{item.title}</h3>
            <p>{item.body}</p>
          </div>
        ))
      ) : (
        <p>No data available.</p> // Message when no data is returned
      )}
    </div>
  );
};

export default ViuDataComponent;