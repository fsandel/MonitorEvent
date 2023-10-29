import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./index.css";
import Home from "./routes/Home";
import Admin from "./routes/Admin";
import User from "./routes/User";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/user/:userId" element={<User />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
