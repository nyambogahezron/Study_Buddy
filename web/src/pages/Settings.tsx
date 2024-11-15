
export default function Settings() {
  return (
    <main>
      <div className='customize-theme'>
        <div className='card'>
          <h2>Customize Your View</h2>

          {/* <!-- primary color --> */}
          <div className='color'>
            <h4>Primary Color</h4>
            <div className='choose-color'>
              <span className='color-1 active'></span>
              <span className='color-2'></span>
              <span className='color-3'></span>
              <span className='color-4'> </span>
              <span className='color-5'></span>
            </div>
          </div>

          {/* <!-- background color  --> */}

          <div className='background'>
            <h4>Background Color</h4>
            <div className='choose-bg'>
              <div className='bg-1 active'>
                <span></span>
                <h5 className='bg-1'>Light</h5>
              </div>

              <div className='bg-2'>
                <span></span>
                <h5 className='bg-2'>Dim</h5>
              </div>
              <div className='bg-3'>
                <span></span>
                <h5 className='bg-3'>Dark</h5>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
