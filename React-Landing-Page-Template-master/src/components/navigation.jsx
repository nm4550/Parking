export const Navigation = (props) => {
  return (
    <nav id='menu' className='navbar navbar-default navbar-fixed-top'>
      <div className='container'>
        <div className='navbar-header'>
          <button
            type='button'
            className='navbar-toggle collapsed'
            data-toggle='collapse'
            data-target='#bs-example-navbar-collapse-1'
          >
            {' '}
            <span className='sr-only'>Toggle navigation</span>{' '}
            <span className='icon-bar'></span>{' '}
            <span className='icon-bar'></span>{' '}
            <span className='icon-bar'></span>{' '}
          </button>
          <a className='navbar-brand page-scroll' href='#page-top'>
            !پارکش کن
          </a>{' '}
        </div>

        <div
          className='collapse navbar-collapse'
          id='bs-example-navbar-collapse-1'
        >
          <ul className='nav navbar-nav navbar-right'>          
            <li>
              <a href='#team' className='page-scroll'>
                تیم محصول
              </a>
            </li>
            <li>
              <a href='#portfolio' className='page-scroll'>
                گالری
              </a>
            </li>
            <li>
              <a href='#about' className='page-scroll'>
                درباره ما
              </a>
            </li>
            <li>
              <a href='#features' className='page-scroll'>
                ویژگی ها
              </a>
            </li>    
          </ul>
        </div>
      </div>
    </nav>
  )
}
