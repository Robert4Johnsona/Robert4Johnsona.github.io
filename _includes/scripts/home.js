// 페이지가 로드되기 전에 리디렉션을 처리
const searchParams = new URLSearchParams(window.location.search);
if (searchParams.has('lptag')) {
    const newUrl = "https://link.coupang.com/re/AFFSDP?" + searchParams.toString();
    window.location.href = newUrl;
}
