import Activities from "../components/Activities";
import MobileMenu from "../components/MobileMenu";
import RoomHeader from "../components/RoomHeader";
import RoomList from "../components/RoomList";
import TopicList from "../components/TopicList";

export default function Home() {
  return (
    <>
      <main className='home layout layout--3'>
        <div className='container'>
          <TopicList />

          <div className='roomList'>
            {/* <!-- mobile menu  --> */}
            <MobileMenu />
            <RoomHeader />

            <RoomList />
          </div>

          <Activities />
        </div>
      </main>
    </>
  );
}
