let root

const hash2ModuleFile = {
  '/home'      : '/home.js',
  '/deposit'    : '/deposit.js',
  '/svc_record'    : '/svc_record.js',
  '/charger'   : {fileName: '/device.js', className:'Charger'},
  '/carwasher' : {fileName: '/device.js', className:'CarWasher'},
  '/locker'    : {fileName: '/device.js', className:'Locker'},
  '/my_charger'   : {fileName: '/my_dev_history.js', className:'MyHistory_Charger'},
  '/my_carwasher' : {fileName: '/my_dev_history.js', className:'MyHistory_CarWasher'},
  '/my_lockers' : {fileName: '/my_dev_history.js', className:'MyHistory_Locker'},
}

let hashEntries = Object.entries(hash2ModuleFile)

const ModuleFile2Element = {} 

async function renderMain(){
  let url = window.location.hash.slice(1)

  let componentDesc = null // 组件描述

  //  使用for ... of 遍历数组
  for (let [key, value] of hashEntries) {
    if (url.startsWith(key)){
      componentDesc = value
      break
    }    
  }

  // hash2ModuleFile中没有该配置
  if (!componentDesc){
    alert('该功能未实现')
    return
  }

  
  // 尝试从模块表中获取已经加载的模块
  let element = ModuleFile2Element[url]

  // 未加载过
  if (!element) {    
    // 只是模块文件路径， 组件肯定是缺省导出
    if(typeof componentDesc === 'string'){
      // let { default: DClass }  = await import(componentDesc);
      // Component = DClass
      Component  = (await import(componentDesc)).default;
    }
    // 否则，是命名导出
    else{
      Component  = (await import(componentDesc.fileName))[componentDesc.className]
    }

    element = React.createElement(Component)
    
    ModuleFile2Element[url] = element
  }  

  root.render(element);

}

window.onload = function(){
  
  window.addEventListener('hashchange', function() {
    renderMain()
  });
  
  root = ReactDOM.createRoot(document.querySelector('main'));
  
  renderMain(root);


}

