import { VisualizerWebAppPage } from './app.po';

describe('visualizer-web-app App', () => {
  let page: VisualizerWebAppPage;

  beforeEach(() => {
    page = new VisualizerWebAppPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
