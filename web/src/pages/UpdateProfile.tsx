import { Link } from 'react-router-dom';

export default function UpdateProfile() {
  return (
    <main className='settings-page layout'>
      <div className='container'>
        <div className='layout__box'>
          <div className='layout__boxHeader'>
            <div className='layout__boxTitle'>
              <Link to='/'>
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
              <h3>Profile</h3>
            </div>
          </div>

          <div className='settings layout__body'>
            <div className='settings__avatar'>
              <div className='avatar avatar--large active'>
                <img src='./assets/images/user.png' id='preview-avatar' />
              </div>
            </div>
            <form className='form' action='#'>
              <div className='form__group form__avatar'>
                <label htmlFor='avatar'>Upload Avatar</label>
                <input
                  className='form__hide'
                  required
                  type='file'
                  name='avatar'
                  id='avatar'
                  accept='image/png, image/gif, image/jpeg'
                />
              </div>
              <div className='form__group'>
                <label htmlFor='name'>Full Name</label>
                <input
                  id='fullname'
                  name='fullname'
                  type='text'
                  placeholder='e.g. john_doe'
                  value='john_doe'
                />
              </div>
              <div className='form__group'>
                <label htmlFor='username'>Username</label>
                <input
                  id='username'
                  name='username'
                  type='text'
                  placeholder='e.g. @john_doe'
                  value='@john_doe'
                />
              </div>
              <div className='form__group'>
                <label htmlFor='email'>Email</label>
                <input
                  id='email'
                  name='email'
                  type='email'
                  placeholder='e.g. user@domain.com'
                />
              </div>
              <div className='form__group'>
                <label htmlFor='about'>About</label>
                <textarea
                  name='about'
                  id='about'
                  placeholder='Write about yourself...'
                ></textarea>
              </div>
              <div className='form__action'>
                <a className='btn btn--dark' href='profile.html'>
                  Cancel
                </a>
                <button className='btn btn--main' type='submit'>
                  Update Profile
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </main>
  );
}
