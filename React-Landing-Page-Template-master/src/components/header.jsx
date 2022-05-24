import '../css/Global.css';
export const Header = (props) => {
  return (
    <header id='header'>
      <div className='intro'>
        <div className='overlay'>
          <div className='container'>
            <div className='row'>
              <div className='col-md-8 col-md-offset-2 intro-text'>
                <h1>
                  {props.data ? props.data.title : 'Loading'}
                  <span></span>
                </h1>
                <p>{props.data ? props.data.paragraph : 'Loading'}</p>

                

                <div  className="containerButtonGlobal">
                  <a className="ButtonGlobal" href="http://localhost:3000/">ورود</a>      
                </div><br/>

                <div className="containerButtonGlobal">
                  <a className="ButtonGlobal" href="http://localhost:3000/Signup">ثبت نام</a>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  )
}
