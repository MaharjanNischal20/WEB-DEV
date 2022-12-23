import React from "react";

class Item extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      clicks: 0,
      remainingClicks: 100,
    };
  }

  clickME() {
    this.setState({
      clicks: this.state.clicks + 1,
      remainingClicks: this.state.remainingClicks - 1,
    });
  }
  render() {
    return (
      <div>
        <h1 onClick={() => this.clickME()}>Hello It's me, {this.props.name}</h1>
        <span>
          {this.state.clicks} is the number of clicks. Remaining{" "}
          {this.state.remainingClicks}
        </span>
      </div>
    );
  }
}
export default Item;
