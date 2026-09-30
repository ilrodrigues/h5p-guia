const navigation = document.querySelector('nav');
const updateHeaderOffset = () => {
  document.documentElement.style.setProperty('--navigation-height', `${navigation.getBoundingClientRect().height}px`);
};
new ResizeObserver(updateHeaderOffset).observe(navigation);
updateHeaderOffset();
