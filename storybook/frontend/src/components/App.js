import React, { useState, useEffect } from "react";
import Scene from "./Scene";

const App = () => {
  const [stories, setStories] = useState([]);

  useEffect(() => {
    fetch("/api/stories/")
      .then((response) => response.json())
      .then((data) => setStories(data));
  }, []);

  return (
    <div>
      {stories.map((story) => (
        <div key={story.id}>
          <h2>{story.title}</h2>
          <Scene />
        </div>
      ))}
    </div>
  );
};

export default App;
