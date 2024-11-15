import { Link } from "react-router-dom";

export default function CreateRoom() {
  return (
    <main className='create-room layout'>
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
              <h3>Create Study Room</h3>
            </div>
          </div>
          <div className='layout__body'>
            <form className='form' action='#'>
              <div className='form__group'>
                <label htmlFor='room_name'>Room Name</label>
                <input
                  id='room_name'
                  name='room_name'
                  type='text'
                  placeholder='E.g. Mastering Python + Django'
                />
              </div>

              <div className='form__group'>
                <label htmlFor='room_topic'>Topic</label>
                <input
                  required
                  type='text'
                  name='topic'
                  id='room_topic'
                  list='topic-list'
                />
                <datalist id='topic-list'>
                  <select id='room_topic'>
                    <option value=''>Select your topic</option>
                    <option value='Python'>Python</option>
                    <option value='Django'>Django</option>
                  </select>
                </datalist>
              </div>

              <div className='form__group'>
                <label htmlFor='room_about'>About</label>
                <textarea
                  name='room_about'
                  id='room_about'
                  placeholder='Write about your study group...'
                ></textarea>
              </div>
              <div className='form__action'>
                <Link className='btn btn--dark' to='/'>
                  Cancel
                </Link>
                <button className='btn btn--main' type='submit'>
                  Create Room
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </main>
  );
}
