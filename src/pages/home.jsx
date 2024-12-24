import React, { useEffect, useState, useContext } from "react";
import { Context } from "../store/appContext.jsx";
import { useTheme } from "next-themes";
import { Button } from "@nextui-org/react";

function Home() {
  const { store, actions } = useContext(Context);
  const { theme, setTheme } = useTheme();
  const [id, setId] = useState(0);

  const createItem = async (item) => {
    const response = await actions.createItem(item);
    console.log(response);
    actions.getItems();
  };

  const deleteItem = async (item_id) => {
    const response = await actions.deleteItem(item_id);
    console.log(response);
    actions.getItems();
  };

  useEffect(() => {
    actions.getItems();
  }, []);

  return (
    <div>
      Hola
    </div>
  );
}

export default Home;
