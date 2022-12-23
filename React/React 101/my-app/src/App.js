// import logo from "./logo.svg";
import "./App.css";
import React from "react";
// import Item from "./myItem";
class FilmItemRow extends React.Component {
  render() {
    return (
      <li>
        <a href={this.props.url}>{this.props.url}</a>
      </li>
    );
  }
}

class Starwars extends React.Component {
  constructor() {
    super();
    this.state = {
      Name: null,
      Height: null,
      Homeworld: null,
      Films: [],
      loadedcharacter: false,
    };
  }

  getNewCharacter() {
    const randomNumber = Math.ceil(Math.random() * 88);
    const url = `https://swapi.dev/api/people/${randomNumber}/`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          Name: data.name,
          Height: data.height,
          Homeworld: data.homeworld,
          Films: data.films,
          loadedcharacter: true,
        });
      });
  }

  render() {
    const movies = this.state.Films.map((film, i) => {
      return <FilmItemRow key={i} url={film} />;
    });
    return (
      <div>
        {this.state.loadedcharacter && (
          // works as if statement
          <div>
            <h1>{this.state.Name}</h1>
            <p>{this.state.Height} cm</p>
            <p>
              <a href={this.state.Homeworld}>Homeworld</a>
            </p>
            <ul>{movies}</ul>
          </div>
        )}
        <button
          type="button"
          className="btn"
          onClick={() => this.getNewCharacter()}
        >
          Randomize Character
        </button>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Starwars />
      </header>
    </div>
  );
}

export default App;
