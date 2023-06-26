'use strict';

const e = React.createElement;

class MyForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        first_name: '',
        last_name: '',
        phone_number: '',
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  

  handleChange(event) {
    this.setState({[event.target.name]: event.target.value});
  }

  handleSubmit(event) {
    console.log('submit');
  }

  render() {

    return (
        <div className="justify-content-center">
            <form className="form justify-content-center" method="post">
                <CSRFToken/>
                <div className={"first-name-wrapper"}>
                    <div className="form-group">
                        <label htmlFor="id_first_name">First Name</label>
                        <input type="text" name="first_name" className="form-control" maxLength="32" required id="id_first_name"
                            autoComplete="off" value={this.state.firstName} onChange={this.handleChange}/>
                    </div>
                </div>
                <div className={"last-name-wrapper"}>
                    <div className="form-group">
                        <label htmlFor="id_last_name">Last Name</label>
                        <input type="text" name="last_name" className="form-control" maxLength="32" required id="id_last_name"
                            autoComplete="off" value={this.state.lastName} onChange={this.handleChange}/>
                    </div>
                </div>
                <div className={"phone-wrapper"}>
                    <div className="form-group">
                        <label htmlFor="id_phone_number">Phone Number</label>
                        <input type="text" name="phone_number" className="form-control" maxLength="128" required id="id_phone_number"
                            autoComplete="off" value={this.state.email} onChange={this.handleChange}/>
                    </div>
                </div>
                <div className={"submit-wrapper"}>
                    <button type="submit" className="btn btn-primary" name="action" value="submit">Submit</button>
                </div>
                
            </form>
        </div>
    );
  }
}

ReactDOM.render(<MyForm/>, document.getElementById('create-patient-form'));
