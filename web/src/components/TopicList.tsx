export default function TopicList() {
  return (
    <div className='topics'>
      <div className='topics__header'>
        <h2>Browse Topics</h2>
      </div>
      <ul className='topics__list'>
        <li>
          <a href='/' className='active'>
            All <span>553</span>
          </a>
        </li>
        <li>
          <a href='/'>
            Python <span>232</span>
          </a>
        </li>
        <li>
          <a href='/'>
            JavaScript <span>122</span>
          </a>
        </li>
        <li>
          <a href='/'>
            React <span>57</span>
          </a>
        </li>
        <li>
          <a href='/'>
            Database <span>90</span>
          </a>
        </li>
        <li>
          <a href='/'>
            AI <span>20</span>
          </a>
        </li>
        <li>
          <a href='/'>
            Computer Sc <span>91</span>
          </a>
        </li>
        <li>
          <a href='/'>
            Linux <span>40</span>
          </a>
        </li>
      </ul>
      <a className='btn btn--link' href='topics.html'>
        More
        <svg
          version='1.1'
          xmlns='http://www.w3.org/2000/svg'
          width='32'
          height='32'
          viewBox='0 0 32 32'
        >
          <title>chevron-down</title>
          <path d='M16 21l-13-13h-3l16 16 16-16h-3l-13 13z'></path>
        </svg>
      </a>
    </div>
  );
}
