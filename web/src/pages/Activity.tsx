import { Link } from 'react-router-dom';

export default function Activity() {
  return (
    <main className='activities-page layout'>
      <div className='container'>
        <div className='layout__box'>
          <div className='layout__boxHeader'>
            <div className='layout__boxTitle'>
              <Link to='/index'>
                <svg
                  version='1.1'
                  xmlns='http://www.w3.org/2000/svg'
                  width='32'
                  height='32'
                  viewBox='0 0 32 32'
                >
                  <title>arrow-left</title>
                  <path d='M13.723 2.286l-13.723 13.714 13.719 13.714 1.616-1.611-10.96-10.96h27.625v-2.286h-27.625l10.965-10.965-1.616-1.607z'></path>
                </svg>
              </Link>
              <h3>Recent Activities</h3>
            </div>
          </div>

          <div className='layout__body'>
            {/* <!-- list item start  --> */}
            <div className='activities__box'>
              <div className='activities__boxHeader roomListRoom__header'>
                <Link to='/profile' className='roomListRoom__author'>
                  <div className='avatar avatar--small'>
                    <img src='./assets/images/user.png' />
                  </div>
                  <p>
                    @john_doe
                    <span>5 days ago</span>
                  </p>
                </Link>
                <div className='roomListRoom__actions'>
                  <Link to='/#'>
                    <svg
                      version='1.1'
                      xmlns='http://www.w3.org/2000/svg'
                      width='32'
                      height='32'
                      viewBox='0 0 32 32'
                    >
                      <title>remove</title>
                      <path d='M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z'></path>
                    </svg>
                  </Link>
                </div>
              </div>
              <div className='activities__boxContent'>
                <p>
                  {' '}
                  <span>replied to post </span>{' '}
                  <span>
                    "<Link to='/room'>100 Days of code challenge!</Link>”
                  </span>
                </p>
                <div className='activities__boxRoomContent'>
                  Ill have to try this sometime. Really like this idea. Wanna
                  talk about it? I m
                </div>
              </div>
            </div>
            {/* <!-- list item ends  --> */}
            {/* <!-- list item start  --> */}
            <div className='activities__box'>
              <div className='activities__boxHeader roomListRoom__header'>
                <Link to='/profile' className='roomListRoom__author'>
                  <div className='avatar avatar--small'>
                    <img src='./assets/images/user.png' />
                  </div>
                  <p>
                    @john_doe
                    <span>5 days ago</span>
                  </p>
                </Link>
                <div className='roomListRoom__actions'>
                  <Link to='/#'>
                    <svg
                      version='1.1'
                      xmlns='http://www.w3.org/2000/svg'
                      width='32'
                      height='32'
                      viewBox='0 0 32 32'
                    >
                      <title>remove</title>
                      <path d='M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z'></path>
                    </svg>
                  </Link>
                </div>
              </div>
              <div className='activities__boxContent'>
                <p>
                  {' '}
                  <span>replied to post </span>{' '}
                  <span>
                    "<Link to='/room'>100 Days of code challenge!</Link>”
                  </span>
                </p>
                <div className='activities__boxRoomContent'>
                  Ill have to try this sometime. Really like this idea. Wanna
                  talk about it? I m
                </div>
              </div>
            </div>
            {/* <!-- list item ends  --> */}
            {/* <!-- list item start  --> */}
            <div className='activities__box'>
              <div className='activities__boxHeader roomListRoom__header'>
                <Link to='/profile' className='roomListRoom__author'>
                  <div className='avatar avatar--small'>
                    <img src='./assets/images/user.png' />
                  </div>
                  <p>
                    @john_doe
                    <span>5 days ago</span>
                  </p>
                </Link>
                <div className='roomListRoom__actions'>
                  <Link to='/#'>
                    <svg
                      version='1.1'
                      xmlns='http://www.w3.org/2000/svg'
                      width='32'
                      height='32'
                      viewBox='0 0 32 32'
                    >
                      <title>remove</title>
                      <path d='M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z'></path>
                    </svg>
                  </Link>
                </div>
              </div>
              <div className='activities__boxContent'>
                <p>
                  {' '}
                  <span>replied to post </span>{' '}
                  <span>
                    "<Link to='/room'>100 Days of code challenge!</Link>”
                  </span>
                </p>
                <div className='activities__boxRoomContent'>
                  Ill have to try this sometime. Really like this idea. Wanna
                  talk about it? I m
                </div>
              </div>
            </div>
            {/* <!-- list item ends  --> */}
            {/* <!-- list item start  --> */}
            <div className='activities__box'>
              <div className='activities__boxHeader roomListRoom__header'>
                <Link to='/profile' className='roomListRoom__author'>
                  <div className='avatar avatar--small'>
                    <img src='./assets/images/user.png' />
                  </div>
                  <p>
                    @john_doe
                    <span>5 days ago</span>
                  </p>
                </Link>
                <div className='roomListRoom__actions'>
                  <Link to='/#'>
                    <svg
                      version='1.1'
                      xmlns='http://www.w3.org/2000/svg'
                      width='32'
                      height='32'
                      viewBox='0 0 32 32'
                    >
                      <title>remove</title>
                      <path d='M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z'></path>
                    </svg>
                  </Link>
                </div>
              </div>
              <div className='activities__boxContent'>
                <p>
                  {' '}
                  <span>replied to post </span>{' '}
                  <span>
                    "<Link to='/room'>100 Days of code challenge!</Link>”
                  </span>
                </p>
                <div className='activities__boxRoomContent'>
                  Ill have to try this sometime. Really like this idea. Wanna
                  talk about it? I m
                </div>
              </div>
            </div>
            {/* <!-- list item ends  --> */}
          </div>
        </div>
      </div>
    </main>
  );
}
