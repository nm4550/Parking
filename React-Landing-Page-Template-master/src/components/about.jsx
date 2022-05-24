export const About = (props) => {
  return (
    <div  id="about" style={{direction:"rtl"}}>
      <div className="container" style={{direction:"rtl"}}>
        <div className="row" style={{direction:"rtl"}}>
          
          <div className="col-xs-12 col-md-6" style={{direction:"rtl"}}>
            <br/><br/><div className="about-text">
              <h2>درباره ما</h2>
              <p>{props.data ? props.data.paragraph : "loading..."}</p>
              <h3>چرا باید ما را انتخاب کنید؟</h3>
              <div className="list-style">
                <div className="col-lg-6 col-sm-6 col-xs-12">
                  <ul>
                    {props.data
                      ? props.data.Why.map((d, i) => (
                          <li key={`${d}-${i}`}>{d}</li>
                        ))
                      : "loading"}
                  </ul>
                </div>
                <div className="col-lg-6 col-sm-6 col-xs-12">
                  <ul>
                    {props.data
                      ? props.data.Why2.map((d, i) => (
                          <li key={`${d}-${i}`}> {d}</li>
                        ))
                      : "loading"}
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div className="col-xs-12 col-md-6" style={{direction:"rtl"}}>
            {" "}
            <img src="img/about.jpg" className="img-responsive" alt="" />{" "}
          </div>
        </div>
      </div>
    </div>
  );
};
