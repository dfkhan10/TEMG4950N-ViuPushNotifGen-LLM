import TextBox from "../components/TextBox";
import React, { useEffect, useState } from "react";

const ViuDataContext = React.createContext({
  viuData: [], fetchViudata: () => {}
})

export const Homepage = () => {
  //Call a get api to retrieve viu data for dropdown menus  of cast and show
  const [viuDatas, setViuDatas] = useState([])

  const fetchViuData = async () => {
    const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/viuData`);
    const data = await response.json()
    console.log(data)
    setViuDatas(data.key)
  }

  useEffect(() => { fetchViuData() }, [])

  return (
    <div className="container px-4 md:px-0">
      <span>{viuDatas}</span>
      <TextBox />
    </div>
  );
}
